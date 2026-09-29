"""
Resilient client interface for Kimi WebBridge Daemon.
Manages HTTP command dispatch, tab navigation, script evaluation, and error handling.
"""

import urllib.request
import json
import time
from typing import Any, Dict, Optional
from config import DAEMON_URL, STATUS_URL, SESSION_NAME, DEFAULT_TIMEOUT

class BridgeClient:
    def __init__(self, session_name: str = SESSION_NAME, daemon_url: str = DAEMON_URL, timeout: int = DEFAULT_TIMEOUT):
        self.session_name = session_name
        self.daemon_url = daemon_url
        self.timeout = timeout

    def send_command(self, action: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Dispatches an action payload to the Kimi WebBridge HTTP daemon.
        """
        payload = {
            "action": action,
            "args": args,
            "session": self.session_name
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.daemon_url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw_body = resp.read().decode("utf-8")
                return json.loads(raw_body)
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def navigate(self, url: str, new_tab: bool = False, group_title: Optional[str] = None) -> bool:
        """
        Navigates the browser session to the target URL.
        """
        args: Dict[str, Any] = {"url": url, "newTab": new_tab}
        if group_title:
            args["group_title"] = group_title
        resp = self.send_command("navigate", args)
        return resp.get("ok", False)

    def evaluate(self, js_code: str) -> Any:
        """
        Evaluates JavaScript asynchronously in the active page context.
        """
        resp = self.send_command("evaluate", {"code": js_code})
        if not resp.get("ok", False):
            return {"error": resp.get("error", "Evaluation failed")}
        val = resp.get("data", {}).get("value")
        if isinstance(val, str):
            try:
                return json.loads(val)
            except Exception:
                return val
        return val

    def is_daemon_alive(self) -> bool:
        """
        Checks if the local WebBridge daemon is active and responding.
        """
        try:
            with urllib.request.urlopen(STATUS_URL, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("running", False)
        except Exception:
            return False

    def is_extension_connected(self) -> bool:
        """
        Checks if the browser extension WebSocket is attached to the daemon.
        """
        try:
            with urllib.request.urlopen(STATUS_URL, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("running", False) and data.get("extension_connected", False)
        except Exception:
            return False
