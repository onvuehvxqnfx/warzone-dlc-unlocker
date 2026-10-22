"""Thin CLI handler used by the JS shim in tools/."""
import json
import sys

from ..core.unlocker import DLCCheckUnlocker
from ..core.entitlement import EntitlementPatcher
from ..config.loader import load_config


def dispatch(argv):
    cmd = argv[0] if argv else "status"
    cfg = load_config("config/default.toml")
    if cmd == "unlock":
        return {"unlocked": DLCCheckUnlocker(cfg).scan_and_unlock()}
    if cmd == "patch":
        return {"patched": EntitlementPatcher(cfg).apply_patches()}
    return {"status": "ok", "version": "2.4.1"}


if __name__ == "__main__":
    print(json.dumps(dispatch(sys.argv[1:])))