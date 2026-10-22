# Contributing to warzone-dlc-unlocker

Thanks for your interest. This is a hobbyist educational project for
researching how Warzone DLC entitlement checks work locally.

## Workflow
1. Fork and clone.
2. `pip install -r requirements.txt`
3. Run `python -m warzone_dlc_unlocker --dry-run`
4. Open a PR against `main` with a clear description of the DLC id or
   entitlement offset you're targeting.

## Rules
- Never commit real `entitlements.bin` or `license.dat` dumps.
- Keep patches reversible — every write should go through
  `utils/memory.write_bytes` so backups stay valid.
- Add a test under `tests/` for any new offset constants.