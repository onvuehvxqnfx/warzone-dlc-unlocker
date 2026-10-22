import argparse
import logging
import sys

from .core.unlocker import DLCCheckUnlocker
from .core.entitlement import EntitlementPatcher
from .config.loader import load_config
from .utils.logging_setup import setup_logging


def main(argv=None):
    parser = argparse.ArgumentParser(prog="warzone-dlc-unlocker")
    parser.add_argument("--config", default="config/default.toml")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    setup_logging(verbose=args.verbose)

    log = logging.getLogger("wzdlc")
    log.info("warzone-dlc-unlocker starting (dry_run=%s)", args.dry_run)

    unlocker = DLCCheckUnlocker(cfg)
    patcher = EntitlementPatcher(cfg)

    unlocked = unlocker.scan_and_unlock(dry_run=args.dry_run)
    patched = patcher.apply_patches(dry_run=args.dry_run)

    log.info("unlocked=%d patched=%d", unlocked, patched)
    return 0


if __name__ == "__main__":
    sys.exit(main())