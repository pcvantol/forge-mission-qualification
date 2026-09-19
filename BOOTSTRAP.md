# Qualification repository bootstrap

This repository is the public, synthetic target for the isolated Forge and
Engineering Platform Mission qualification. The protected `main` branch is the
delivery baseline.

The installed `mission-parser` entrypoint is defined in `mission_parser/cli.py`.
The acceptance controls in `acceptance/` exercise its malformed-record and
valid-record behavior. Run the complete acceptance surface, including the
nonstandard grouping module name, with
`python3 -m unittest discover -s acceptance -t . -p '*.py'`.

Changes to this repository are delivered through protected pull requests with
the required smoke check. Operational credentials, receipts, local paths, and
Mission runtime state do not belong in this repository.

## Current engineering state

Positive quantity scaling is implemented for installed single-record and batch
modes. Installed batch mode can additionally group repeated names in first-seen
order after scaling, while single-mode and ungrouped behavior remain unchanged.
Malformed records, non-positive quantities, and non-positive scales remain
rejected.

Optional `--prefix` handling is present on protected `main` through
implementation PR #25. It applies to installed single-record and batch name
output while preserving existing behavior when omitted; it does not add
selection behavior. Governance-only Finalization for run
`inbox-8b0ce51bb41e42179e886da4bd33ceb9` is pending through Finalization PR #26.
Exceptionally large integer input remains a known non-blocking availability
observation because input size is not explicitly bounded. Prompt History
remains an immutable Engineering Platform record and is not copied into this
repository.
