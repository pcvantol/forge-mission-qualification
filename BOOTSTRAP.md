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

Batch selection on transformed names after optional prefixing is present on
protected `main` through implementation PR #28. Selection preserves matching
record order, composes with scaling and grouping, and is available only in
batch mode; no limiting behavior was introduced. Its governance-only
Finalization is merged through Finalization PR #29 for run
`inbox-6e5a40147c3e49b982377aa81e5ff664`. Exceptionally large integer input
remains a known non-blocking availability observation because input size is not
explicitly bounded. Prompt History remains an immutable Engineering Platform
record and is not copied into this repository.
