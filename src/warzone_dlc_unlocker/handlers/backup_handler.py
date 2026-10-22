import logging

from ..config.schema import Config
from ..utils.backup import snapshot

log = logging.getLogger(__name__)


def run_backup(cfg: Config) -> str:
    if not cfg.auto_backup:
        log.info("auto-backup disabled, skipping")
        return ""
    path = snapshot(cfg.game_root, cfg.backup_dir, ["entitlements.bin", "license.dat"])
    log.info("snapshot written to %s", path)
    return str(path)