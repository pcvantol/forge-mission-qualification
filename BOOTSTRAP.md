# Qualification repository bootstrap

This repository is the public, synthetic target for the isolated Forge and
Engineering Platform Mission qualification. The protected `main` branch is the
delivery baseline.

The installed `mission-parser` entrypoint is defined in `mission_parser/cli.py`.
The acceptance controls in `acceptance/` exercise its malformed-record and
valid-record behavior. Run them with `python -m unittest discover -s acceptance`.

Changes to this repository are delivered through protected pull requests with
the required smoke check. Operational credentials, receipts, local paths, and
Mission runtime state do not belong in this repository.

## Current engineering state

Positive quantity scaling is implemented for installed single-record and batch
modes by implementation PR #9. Omitting `--scale` preserves canonical unscaled
output, while malformed records, non-positive quantities, and non-positive
scales remain rejected.

The implementation and governance handoff for run
`inbox-3ce6c0480ba64f208b05571acffba732` are present on protected `main` through
Finalization PR #10. Prompt History remains an immutable Engineering Platform
record and is not copied into this repository.
