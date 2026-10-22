# Known Entitlement Offsets

| Field              | Offset | Length |
|--------------------|--------|--------|
| ownership bitfield | 0x1A8  | 0x40   |
| signature          | 0x2E8  | 0x10   |

These offsets are for the 2026 Warzone client build. They change between
seasons — update `core/unlocker.py` and `core/entitlement.py` when the
client is patched.