"""Entitlement patcher - rewrites signed entitlement records.

Handles the local license signature bypass so the game client trusts the
patched DLC ownership bitfield written by DLCCheckUnlocker.
"""
import hashlib
import logging
import struct
from pathlib import Path

from ..config.schema import Config
from ..utils.memory import read_bytes, write_bytes

log = logging.getLogger(__name__)

KNOWN_DLC_IDS = [
    "wz_dlc_s1_battlepass",
    "wz_dlc_s2_battlepass",
    "wz_dlc_s3_battlepass",
    "wz_dlc_operator_ghost",
    "wz_dlc_operator_soap",
    "wz_dlc_weapon_pack_meta",
    "wz_dlc_weapon_pack_retro",
    "wz_dlc_skin_blackops",
    "wz_dlc_tracer_pack_cyan",
    "wz_dlc_execution_pack_stealth",
]

# Signature is stored as 16-byte MD5-like digest right after the entitlement record.
SIG_OFFSET = 0x2E8
SIG_LEN = 16


class EntitlementPatcher:
    def __init__(self, config: Config):
        self.config = config
        self.license_path = Path(config.game_root) / "license.dat"

    def _recompute_signature(self, record: bytes) -> bytes:
        return hashlib.md5(record).digest()[:SIG_LEN]

    def apply_patches(self, dry_run: bool = False) -> int:
        if not self.license_path.exists():
            log.warning("license.dat not found at %s", self.license_path)
            return 0

        blob = bytearray(read_bytes(self.license_path))
        if len(blob) < SIG_OFFSET + SIG_LEN:
            raise ValueError("license.dat too small to patch")

        record = bytes(blob[:SIG_OFFSET])
        new_sig = self._recompute_signature(record)
        old_sig = bytes(blob[SIG_OFFSET:SIG_OFFSET + SIG_LEN])

        if new_sig == old_sig:
            log.debug("license signature already valid")
            return 0

        if dry_run:
            log.info("[dry-run] would rewrite license signature")
            return 1

        blob[SIG_OFFSET:SIG_OFFSET + SIG_LEN] = new_sig
        write_bytes(self.license_path, bytes(blob))
        log.info("rewrote license signature")
        return 1