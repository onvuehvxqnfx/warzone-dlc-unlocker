"""File-mapped memory read/write helpers (no live process injection)."""
from pathlib import Path


def read_bytes(path: Path) -> bytes:
    return Path(path).read_bytes()


def write_bytes(path: Path, data: bytes) -> None:
    p = Path(path)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(p)