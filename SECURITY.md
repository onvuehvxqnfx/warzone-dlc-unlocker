# Security Policy

This tool modifies local game files only. It does **not** perform any
network calls, process injection, or anti-cheat bypass at runtime.

## Reporting
If you find a bug that could corrupt a user's `entitlements.bin` or
`license.dat`, please open a private security advisory rather than a
public issue.

## Scope
- In scope: file parsing, backup integrity, dry-run guarantees.
- Out of scope: server-side entitlement validation, account bans
  resulting from offline patching.