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
modes. Installed batch mode can additionally group repeated names in first-seen
order after scaling, while single-mode and ungrouped behavior remain unchanged.
Malformed records, non-positive quantities, and non-positive scales remain
rejected.

The grouping implementation is present on protected `main` through
implementation PR #21. Governance-only Finalization for run
`inbox-1dcad7fc8bc642309bb040b0d6e56416` is pending through its dedicated draft
Finalization PR. Prompt History remains an immutable Engineering Platform record
and is not copied into this repository.
