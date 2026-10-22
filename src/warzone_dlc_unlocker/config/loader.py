import tomllib
from pathlib import Path

from .schema import Config


def load_config(path: str) -> Config:
    p = Path(path)
    if not p.exists():
        return Config()
    with p.open("rb") as f:
        data = tomllib.load(f)
    return Config(
        game_root=data.get("paths", {}).get("game_root", Config.game_root),
        backup_dir=data.get("paths", {}).get("backup_dir", Config.backup_dir),
        auto_backup=data.get("options", {}).get("auto_backup", True),
        verify_after_patch=data.get("options", {}).get("verify_after_patch", True),
        log_level=data.get("logging", {}).get("level", "INFO"),
    )