import struct
from pathlib import Path

from warzone_dlc_unlocker.core.unlocker import (
    DLCCheckUnlocker,
    OWNERSHIP_BITFIELD_OFFSET,
    OWNERSHIP_BITFIELD_LEN,
)
from warzone_dlc_unlocker.config.schema import Config


def test_unlock_sets_all_bits(tmp_path: Path):
    game_root = tmp_path / "game"
    game_root.mkdir()
    blob = bytearray(0x400)
    (game_root / "entitlements.bin").write_bytes(bytes(blob))

    cfg = Config(game_root=str(game_root))
    n = DLCCheckUnlocker(cfg).scan_and_unlock(dry_run=False)
    assert n > 0

    patched = (game_root / "entitlements.bin").read_bytes()
    bitfield = patched[OWNERSHIP_BITFIELD_OFFSET:OWNERSHIP_BITFIELD_OFFSET + OWNERSHIP_BITFIELD_LEN]
    assert sum(bin(b).count("1") for b in bitfield) >= n


def test_dry_run_does_not_write(tmp_path: Path):
    game_root = tmp_path / "game"
    game_root.mkdir()
    original = bytes(0x400)
    (game_root / "entitlements.bin").write_bytes(original)

    cfg = Config(game_root=str(game_root))
    DLCCheckUnlocker(cfg).scan_and_unlock(dry_run=True)
    assert (game_root / "entitlements.bin").read_bytes() == original