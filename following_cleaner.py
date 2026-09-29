"""
Following Cleaner Module.
Audits the authenticated user's Following list, identifies political/news accounts, and executes blocks.
"""

import time
import sys
from typing import List, Dict, Any
from bridge_client import BridgeClient
from filter_rules import ContentFilter

AUDIT_FOLLOWING_JS = """
(async () => {
  const cells = Array.from(document.querySelectorAll('[data-testid="UserCell"]'));
  return JSON.stringify(cells.map(cell => {
    const text = cell.innerText || '';
    const match = text.match(/@([A-Za-z0-9_]+)/);
    return {
      handle: match ? match[1] : null,
      raw: text.replace(/\\n+/g, ' | ')
    };
  }).filter(c => c.handle));
})()
"""

BLOCK_PROFILE_JS = """
(async () => {
  const start = Date.now();
  let userActionsBtn = null;
  while (Date.now() - start < 5000) {
    const blockedBtn = document.querySelector('[data-testid$="-unblock"], [role="button"][data-testid*="unblock"]');
    if (blockedBtn) {
      return JSON.stringify({ status: "already_blocked" });
    }
    userActionsBtn = document.querySelector('[data-testid="userActions"]');
    if (userActionsBtn) break;
    await new Promise(r => setTimeout(r, 200));
  }

  if (!userActionsBtn) {
    const isSuspendedOrNotFound = document.body.innerText.includes('This account doesn’t exist') ||
                                  document.body.innerText.includes('Account suspended');
    if (isSuspendedOrNotFound) {
      return JSON.stringify({ status: "account_unavailable" });
    }
    return JSON.stringify({ status: "no_actions_btn" });
  }

  userActionsBtn.click();
  await new Promise(r => setTimeout(r, 450));

  const menuItems = Array.from(document.querySelectorAll('[role="menuitem"]'));
  const blockItem = document.querySelector('[data-testid="block"], [role="menuitem"][data-testid*="block"]') ||
                    menuItems.find(m => m.innerText && m.innerText.includes('Block'));
  if (!blockItem) {
    return JSON.stringify({ status: "no_block_menuitem" });
  }

  blockItem.click();
  await new Promise(r => setTimeout(r, 450));

  const confirmBtn = document.querySelector('[data-testid="confirmationSheetConfirm"]');
  if (confirmBtn) {
    confirmBtn.click();
    await new Promise(r => setTimeout(r, 800));
  }

  const verifyBlocked = document.querySelector('[data-testid$="-unblock"], [role="button"][data-testid*="unblock"]');
  return JSON.stringify({ status: verifyBlocked ? "blocked_successfully" : "blocked_unconfirmed" });
})()
"""

class FollowingCleaner:
    def __init__(self, client: BridgeClient):
        self.client = client
        self.filter = ContentFilter()

    def clean_following(self, target_handles: List[str]) -> Dict[str, Any]:
        """
        Iterates over targeted handles and blocks them sequentially.
        """
        results = []
        print(f"[*] Starting Following purge for {len(target_handles)} identified accounts...")

        for idx, handle in enumerate(target_handles, 1):
            clean_handle = handle.lstrip("@").strip()
            url = f"https://x.com/{clean_handle}"
            prefix = f"[{idx}/{len(target_handles)}] @{clean_handle}: "

            try:
                self.client.navigate(url, new_tab=False)
                time.sleep(2.0)

                res = self.client.evaluate(BLOCK_PROFILE_JS)
                status = res.get("status", "unknown") if isinstance(res, dict) else str(res)
                results.append({"handle": clean_handle, "status": status})
                print(f"{prefix}{status}")
            except Exception as e:
                print(f"{prefix}ERROR ({e})")
                results.append({"handle": clean_handle, "status": f"error: {e}"})

            sys.stdout.flush()
            time.sleep(1.2)

        successful = sum(1 for r in results if r["status"] in ("blocked_successfully", "already_blocked", "blocked_unconfirmed"))
        return {"total": len(results), "blocked": successful, "details": results}
