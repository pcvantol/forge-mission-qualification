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
modes by implementation PR #18. Omitting `--scale` preserves canonical unscaled
output, while malformed records, non-positive quantities, and non-positive
scales remain rejected.

The implementation is present on protected `main` through implementation PR
#18, and the governance-only Finalization for run
`inbox-5fa3148502e64093aca6b00c52651211` is merged through Finalization PR #19.
The canonical rolling records are reconciled to that delivered state. Prompt
History remains an immutable Engineering Platform record and is not copied into
this repository.
