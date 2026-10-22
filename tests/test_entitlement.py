from pathlib import Path

from warzone_dlc_unlocker.core.entitlement import EntitlementPatcher, SIG_OFFSET, SIG_LEN
from warzone_dlc_unlocker.config.schema import Config


def test_signature_rewrite(tmp_path: Path):
    game_root = tmp_path / "game"
    game_root.mkdir()
    blob = bytearray(SIG_OFFSET + SIG_LEN + 1)
    (game_root / "license.dat").write_bytes(bytes(blob))

    cfg = Config(game_root=str(game_root))
    n = EntitlementPatcher(cfg).apply_patches()
    assert n == 1

    data = (game_root / "license.dat").read_bytes()
    assert data[SIG_OFFSET:SIG_OFFSET + SIG_LEN] != b"\x00" * SIG_LEN