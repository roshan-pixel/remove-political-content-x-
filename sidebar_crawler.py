"""
Recursive Sidebar Recommendation Crawler.
Visits target accounts, extracts recommendations from 'Who to follow' / 'You might like',
filters them using political/news heuristics, dynamically queues new targets, and blocks them.
"""

import time
import sys
from typing import List, Set, Dict, Any
from bridge_client import BridgeClient
from filter_rules import ContentFilter
from config import SEED_HANDLES

CRAWLER_JS = """
(async () => {
  // 1. Inspect sidebar 'Who to follow' / 'You might like'
  const aside = document.querySelector('aside[aria-label="Who to follow"]') || 
                document.querySelector('aside') || 
                document.querySelector('[data-testid="sidebarColumn"]');
  
  let suggested = [];
  if (aside) {
    const userCells = Array.from(aside.querySelectorAll('[data-testid="UserCell"]'));
    suggested = userCells.map(cell => {
      const text = cell.innerText || '';
      const match = text.match(/@([A-Za-z0-9_]+)/);
      return {
        handle: match ? match[1] : null,
        raw: text.replace(/\\n+/g, ' | ')
      };
    }).filter(x => x.handle);
  }

  // 2. Check if current profile is already blocked
  const blockedBtn = document.querySelector('[data-testid$="-unblock"], [role="button"][data-testid*="unblock"]');
  if (blockedBtn) {
    return JSON.stringify({ status: "already_blocked", suggested: suggested });
  }

  // 3. Find more actions button (three dots)
  const start = Date.now();
  let userActionsBtn = null;
  while (Date.now() - start < 4500) {
    userActionsBtn = document.querySelector('[data-testid="userActions"]');
    if (userActionsBtn) break;
    await new Promise(r => setTimeout(r, 200));
  }

  if (!userActionsBtn) {
    const isSuspendedOrNotFound = document.body.innerText.includes('This account doesn’t exist') ||
                                  document.body.innerText.includes('Account suspended');
    if (isSuspendedOrNotFound) {
      return JSON.stringify({ status: "account_unavailable", suggested: suggested });
    }
    return JSON.stringify({ status: "no_actions_btn", suggested: suggested });
  }

  userActionsBtn.click();
  await new Promise(r => setTimeout(r, 450));

  const menuItems = Array.from(document.querySelectorAll('[role="menuitem"]'));
  const blockItem = document.querySelector('[data-testid="block"], [role="menuitem"][data-testid*="block"]') ||
                    menuItems.find(m => m.innerText && m.innerText.includes('Block'));
  if (!blockItem) {
    return JSON.stringify({ status: "no_block_menuitem", suggested: suggested });
  }

  blockItem.click();
  await new Promise(r => setTimeout(r, 450));

  const confirmBtn = document.querySelector('[data-testid="confirmationSheetConfirm"]');
  if (confirmBtn) {
    confirmBtn.click();
    await new Promise(r => setTimeout(r, 800));
  }

  const verifyBlocked = document.querySelector('[data-testid$="-unblock"], [role="button"][data-testid*="unblock"]');
  const outcome = verifyBlocked ? "blocked_successfully" : "blocked_unconfirmed";

  return JSON.stringify({ status: outcome, suggested: suggested });
})()
"""

class SidebarCrawler:
    def __init__(self, client: BridgeClient, seeds: List[str] = SEED_HANDLES):
        self.client = client
        self.seeds = seeds
        self.filter = ContentFilter()

    def run_discovery_loop(self, max_crawl: int = 250) -> Dict[str, Any]:
        """
        Executes the BFS recommendation discovery and blocking loop.
        """
        queue = list(self.seeds)
        visited: Set[str] = set()
        blocked_records = []
        discovered_count = 0

        print(f"[*] Starting Sidebar Recursive Crawler with {len(queue)} seed accounts...")

        idx = 0
        while idx < len(queue) and idx < max_crawl:
            handle = queue[idx]
            idx += 1
            clean_handle = handle.lstrip("@").strip()

            if clean_handle.lower() in visited or self.filter.is_protected(clean_handle):
                continue

            visited.add(clean_handle.lower())
            url = f"https://x.com/{clean_handle}"
            prefix = f"[{idx}/{len(queue)}] @{clean_handle}: "

            try:
                self.client.navigate(url, new_tab=False)
                time.sleep(2.3)

                res = self.client.evaluate(CRAWLER_JS)
                outcome = res.get("status", "unknown") if isinstance(res, dict) else str(res)
                suggested = res.get("suggested", []) if isinstance(res, dict) else []

                new_additions = []
                for item in suggested:
                    s_handle = item.get("handle")
                    s_raw = item.get("raw", "")
                    if not s_handle:
                        continue
                    s_clean = s_handle.lstrip("@").strip()
                    if s_clean.lower() not in visited and s_clean.lower() not in {q.lower() for q in queue}:
                        if self.filter.is_political_or_news(s_clean, s_raw):
                            queue.append(s_clean)
                            new_additions.append(s_clean)
                            discovered_count += 1

                disc_info = f" -> Discovered: {', '.join(new_additions)}" if new_additions else ""
                print(f"{prefix}{outcome}{disc_info}")
                blocked_records.append({"handle": clean_handle, "status": outcome, "discovered": new_additions})

            except Exception as e:
                print(f"{prefix}ERROR ({e})")
                blocked_records.append({"handle": clean_handle, "status": f"error: {e}", "discovered": []})

            sys.stdout.flush()
            time.sleep(1.3)

        # Return to clean feed
        self.client.navigate("https://x.com/home", new_tab=False)

        successful = sum(1 for r in blocked_records if r["status"] in ("blocked_successfully", "already_blocked", "blocked_unconfirmed"))
        return {
            "processed": len(blocked_records),
            "blocked": successful,
            "discovered": discovered_count,
            "records": blocked_records
        }
