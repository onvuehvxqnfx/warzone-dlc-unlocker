from dataclasses import dataclass, field


@dataclass
class Config:
    game_root: str = r"C:\Program Files\Call of Duty"
    backup_dir: str = "./backups"
    auto_backup: bool = True
    skip_processes: list = field(default_factory=lambda: ["BattleNet.exe", "cod.exe"])
    log_level: str = "INFO"
    verify_after_patch: bool = True