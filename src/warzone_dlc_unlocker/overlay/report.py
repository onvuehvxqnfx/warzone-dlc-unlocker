"""Post-run overlay report rendered as ANSI table."""
from dataclasses import dataclass


@dataclass
class ReportRow:
    dlc_id: str
    owned: bool
    patched: bool


def render(rows: list[ReportRow]) -> str:
    lines = ["DLC ID".ljust(32) + "OWNED  PATCHED"]
    lines.append("-" * 48)
    for r in rows:
        lines.append(f"{r.dlc_id:<32}{'yes' if r.owned else 'no':<7}{'yes' if r.patched else 'no'}")
    return "\n".join(lines)