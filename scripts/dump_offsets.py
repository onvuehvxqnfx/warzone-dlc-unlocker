"""Dev helper - dumps known DLC ids and bitfield offsets for inspection."""
import json

from warzone_dlc_unlocker.core.entitlement import KNOWN_DLC_IDS
from warzone_dlc_unlocker.core.unlocker import (
    OWNERSHIP_BITFIELD_OFFSET,
    OWNERSHIP_BITFIELD_LEN,
)

if __name__ == "__main__":
    print(json.dumps({
        "dlc_ids": KNOWN_DLC_IDS,
        "bitfield_offset": hex(OWNERSHIP_BITFIELD_OFFSET),
        "bitfield_len": hex(OWNERSHIP_BITFIELD_LEN),
    }, indent=2))