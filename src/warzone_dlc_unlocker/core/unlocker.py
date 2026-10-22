"""DLC ownership check unlocker.

Locates the local Warzone entitlement cache and flips the owned flags
for every known DLC package id.
"""
import logging
import struct
from pathlib import Path

from ..config.schema import Config
from ..utils.memory import read_bytes, write_bytes
from .entitlement import KNOWN_DLC_IDS

log = logging.getLogger(__name__)

# Offset of the DLC ownership bitfield inside the entitlement blob.
OWNERSHIP_BITFIELD_OFFSET = 0x1A8
OWNERSHIP_BITFIELD_LEN = 0x40


class DLCCheckUnlocker:
    def __init__(self, config: Config):
        self.config = config
        self.cache_path = Path(config.game_root) / "entitlements.bin"

    def _locate(self) -> Path:
        if not self.cache_path.exists():
            raise FileNotFoundError(f"entitlement cache not found: {self.cache_path}")
        return self.cache_path

    def scan_and_unlock(self, dry_run: bool = False) -> int:
        path = self._locate()
        blob = bytearray(read_bytes(path))
        bitfield = blob[OWNERSHIP_BITFIELD_OFFSET:OWNERSHIP_BITFIELD_OFFSET + OWNERSHIP_BITFIELD_LEN]

        unlocked = 0
        for idx, dlc_id in enumerate(KNOWN_DLC_IDS):
            byte_i = idx // 8
            bit_i = idx % 8
            if byte_i >= len(bitfield):
                break
            if not (bitfield[byte_i] >> bit_i) & 1:
                bitfield[byte_i] |= 1 << bit_i
                unlocked += 1
                log.debug("marked DLC %s as owned", dlc_id)

        if dry_run:
            log.info("[dry-run] would unlock %d DLC entries", unlocked)
            return unlocked

        blob[OWNERSHIP_BITFIELD_OFFSET:OWNERSHIP_BITFIELD_OFFSET + OWNERSHIP_BITFIELD_LEN] = bitfield
        write_bytes(path, bytes(blob))
        log.info("unlocked %d DLC entries in %s", unlocked, path)
        return unlocked