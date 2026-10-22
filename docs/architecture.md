# Architecture

- `src/warzone_dlc_unlocker/core/` — DLC check unlocker + entitlement patcher.
- `src/warzone_dlc_unlocker/config/` — TOML config loader and schema.
- `src/warzone_dlc_unlocker/handlers/` — CLI and backup handlers.
- `src/warzone_dlc_unlocker/overlay/` — ANSI report renderer.
- `src/warzone_dlc_unlocker/utils/` — file memory helpers, logging, backups.
- `tools/` — Node shim to invoke the Python CLI.
- `scripts/` — dev utilities (offset dumper).
- `tests/` — pytest suite covering unlock + signature rewrite.