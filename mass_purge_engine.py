"""
Mass Purge Engine for X Political Content & News Channels.
Systematically purges 1000+ Indian political parties, leaders, state units, news media,
and dynamically queued recommendations while strictly preserving safe tech and financial markets.
"""

import urllib.request
import json
import time
import sys
import os

from mega_political_directory import MEGA_POLITICAL_SEEDS
from filter_rules import ContentFilter
from config import DAEMON_URL, SESSION_NAME

STATE_FILE = r"C:\Users\sgarm\remove-political-content-x-\purge_state.json"
AUDIT_LOG = r"C:\Users\sgarm\AppData\Local\Temp\mass_purge_audit.log"

def send_cmd(action, args):
    req_data = {
        "action": action,
        "args": args,
        "session": SESSION_NAME
    }
    req = urllib.request.Request(
        DAEMON_URL,
        data=json.dumps(req_data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

BLOCK_FAST_JS = """
(async () => {
  // 1. Inspect sidebar 'Who to follow' / 'You might like'
  const aside = document.querySelector('aside[aria-label="Who to follow"]') || 
                document.querySelector('aside') || 
                document.querySelector('[data-testid="sidebarColumn"]');
  let suggested = [];
  if (aside) {
    const cells = Array.from(aside.querySelectorAll('[data-testid="UserCell"]'));
    suggested = cells.map(cell => {
      const match = (cell.innerText || '').match(/@([A-Za-z0-9_]+)/);
      return {
        handle: match ? match[1] : null,
        raw: (cell.innerText || '').replace(/\\n+/g, ' | ')
      };
    }).filter(x => x.handle);
  }

  // 2. Fast check if already blocked
  const blockedBtn = document.querySelector('[data-testid$="-unblock"], [role="button"][data-testid*="unblock"]');
  if (blockedBtn) {
    return JSON.stringify({ status: "already_blocked", suggested: suggested });
  }

  // 3. Find more actions button (three dots)
  const start = Date.now();
  let userActionsBtn = null;
  while (Date.now() - start < 6000) {
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
  return JSON.stringify({ status: verifyBlocked ? "blocked_successfully" : "blocked_unconfirmed", suggested: suggested });
})()
"""

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"visited": [], "queue": list(MEGA_POLITICAL_SEEDS), "blocked_count": 0}

def save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        print(f"[!] Warning: Could not save state file: {e}")

def main(target_limit=1000):
    content_filter = ContentFilter()
    state = load_state()

    visited_set = set(h.lower() for h in state.get("visited", []))
    queue = state.get("queue", list(MEGA_POLITICAL_SEEDS))
    blocked_count = state.get("blocked_count", 0)

    header = f"=== Mass Political & News Purge Engine (Target: {target_limit}+ accounts) ==="
    print(header)
    print(f"[*] Loaded State: {len(visited_set)} already processed, {len(queue)} in active queue, {blocked_count} blocked.")

    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"\n{header}\nSession Started: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    idx = 0
    while idx < len(queue) and len(visited_set) < target_limit:
        handle = queue[idx]
        idx += 1
        clean = handle.lstrip("@").strip()

        if clean.lower() in visited_set or content_filter.is_protected(clean):
            continue

        visited_set.add(clean.lower())
        url = f"https://x.com/{clean}"
        prefix = f"[{len(visited_set)}/{target_limit}] @{clean}: "

        try:
            send_cmd("navigate", {"url": url, "newTab": False})
            time.sleep(2.5)

            res = send_cmd("evaluate", {"code": BLOCK_FAST_JS})
            val_str = res.get("data", {}).get("value", "{}")
            res_data = json.loads(val_str) if isinstance(val_str, str) else val_str

            outcome = res_data.get("status", "unknown")
            suggested = res_data.get("suggested", [])

            # Dynamic sidebar discovery
            new_additions = []
            for item in suggested:
                s_handle = item.get("handle")
                s_raw = item.get("raw", "")
                if not s_handle:
                    continue
                s_clean = s_handle.lstrip("@").strip()
                if s_clean.lower() not in visited_set and s_clean.lower() not in {q.lower() for q in queue}:
                    if content_filter.is_political_or_news(s_clean, s_raw):
                        queue.append(s_clean)
                        new_additions.append(s_clean)

            disc_info = f" (+{len(new_additions)} discovered)" if new_additions else ""
            msg = f"{prefix}{outcome}{disc_info}"

            if outcome in ("blocked_successfully", "already_blocked", "blocked_unconfirmed"):
                blocked_count += 1

            # Update durable state
            state["visited"].append(clean)
            state["queue"] = queue
            state["blocked_count"] = blocked_count
            save_state(state)

        except Exception as e:
            msg = f"{prefix}ERROR ({e})"

        print(msg)
        sys.stdout.flush()

        with open(AUDIT_LOG, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
            f.flush()

        time.sleep(1.2)

    # Return to home
    try:
        send_cmd("navigate", {"url": "https://x.com/home", "newTab": False})
    except Exception:
        pass

    summary = (
        f"\n=== Mass Purge Milestone Reached! ===\n"
        f"Total Accounts Processed: {len(visited_set)}\n"
        f"Total Blocked/Verified  : {blocked_count}\n"
        f"Total In Queue          : {len(queue)}\n"
    )
    print(summary)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(summary + "\n")

if __name__ == "__main__":
    limit = 1000
    if len(sys.argv) > 1:
        try:
            limit = int(sys.argv[1])
        except ValueError:
            pass
    main(target_limit=limit)
