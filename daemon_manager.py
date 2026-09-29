"""
Daemon lifecycle manager for Kimi WebBridge.
Handles independent process startup, health verification, and browser extension detection.
"""

import os
import subprocess
import time
from typing import Dict, Any
from bridge_client import BridgeClient

class DaemonManager:
    def __init__(self):
        self.client = BridgeClient()
        user_profile = os.environ.get("USERPROFILE", "")
        self.daemon_bin = os.path.join(user_profile, ".kimi-webbridge", "bin", "kimi-webbridge.exe")

    def ensure_daemon_running(self) -> bool:
        """
        Ensures the daemon is listening. Starts it detached if stopped.
        """
        if self.client.is_daemon_alive():
            return True

        if not os.path.exists(self.daemon_bin):
            print(f"[!] Daemon binary not found at: {self.daemon_bin}")
            return False

        print("[*] Starting Kimi WebBridge daemon...")
        try:
            # Spawn independently using subprocess DETACHED_PROCESS on Windows
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            subprocess.Popen(
                [self.daemon_bin, "start"],
                creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                close_fds=True
            )
        except Exception as e:
            print(f"[!] Failed to launch daemon: {e}")
            return False

        # Wait up to 10 seconds for daemon to come online
        for _ in range(10):
            time.sleep(1)
            if self.client.is_daemon_alive():
                print("[+] Daemon is now online.")
                return True

        return False

    def wait_for_extension(self, max_wait_seconds: int = 15) -> bool:
        """
        Waits for the browser extension to connect.
        """
        print("[*] Checking browser extension connection...")
        for i in range(max_wait_seconds):
            if self.client.is_extension_connected():
                print("[+] Browser extension attached successfully.")
                return True
            time.sleep(1)
        print("[!] Extension not connected. Please ensure Chrome or Edge is open with the Kimi extension.")
        return False
