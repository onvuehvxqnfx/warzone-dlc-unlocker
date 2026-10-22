"""Snapshot helper - copies entitlement and license files before patching."""
import shutil
import time
from pathlib import Path


def snapshot(game_root: str, backup_dir: str, files: list[str]) -> Path:
    root = Path(game_root)
    out = Path(backup_dir) / f"snapshot_{int(time.time())}"
    out.mkdir(parents=True, exist_ok=True)
    for name in files:
        src = root / name
        if src.exists():
            shutil.copy2(src, out / name)
    return out