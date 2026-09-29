"""
Main entrypoint for X Political Content Remover.
Provides CLI commands to clean following list, launch recursive crawler, or check daemon status.
"""

import argparse
import sys
from bridge_client import BridgeClient
from daemon_manager import DaemonManager
from following_cleaner import FollowingCleaner
from sidebar_crawler import SidebarCrawler
from config import SEED_HANDLES

def main():
    parser = argparse.ArgumentParser(
        description="X Political Content Remover - Autonomous removal of Indian political parties, leaders, subordinates, and news channels from X."
    )
    parser.add_argument("--mode", choices=["crawl", "following", "status"], default="crawl",
                        help="Operation mode: 'crawl' (sidebar recursive loop), 'following' (clean user following list), 'status' (verify bridge connection)")
    parser.add_argument("--max", type=int, default=250, help="Maximum accounts to process in crawler mode")
    args = parser.parse_args()

    dm = DaemonManager()
    if not dm.ensure_daemon_running():
        print("[!] Could not initialize Kimi WebBridge daemon. Exiting.")
        sys.exit(1)

    if not dm.wait_for_extension():
        print("[!] Browser extension is not responding. Ensure your browser is open.")
        sys.exit(1)

    client = BridgeClient()

    if args.mode == "status":
        print("[+] Kimi WebBridge daemon and extension are operational.")
        sys.exit(0)

    elif args.mode == "crawl":
        print(f"[*] Launching Recursive Sidebar Recommendation Crawler (Max: {args.max})...")
        crawler = SidebarCrawler(client=client, seeds=SEED_HANDLES)
        res = crawler.run_discovery_loop(max_crawl=args.max)
        print("\n=== Crawl Execution Summary ===")
        print(f"Total Accounts Processed : {res['processed']}")
        print(f"Total Blocked / Verified : {res['blocked']}")
        print(f"New Entities Discovered  : {res['discovered']}")

    elif args.mode == "following":
        print("[*] Launching Following List Purge...")
        cleaner = FollowingCleaner(client=client)
        # Seed targets for following cleanup
        from config import SEED_HANDLES
        res = cleaner.clean_following(target_handles=SEED_HANDLES[:41])
        print("\n=== Following Purge Summary ===")
        print(f"Total Accounts Processed : {res['total']}")
        print(f"Total Blocked / Verified : {res['blocked']}")

if __name__ == "__main__":
    main()
