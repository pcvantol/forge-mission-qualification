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
modes. Installed batch mode can additionally select, skip, limit, reverse, and
group records, while single-mode and unchanged-option behavior remain intact.
Malformed records, non-positive quantities, and non-positive scales remain
rejected.

Protected `main` includes batch reversal through implementation PR #45 for run
`inbox-ff4da8ed94c0459aa68ca2107e3f3a34`. In batch mode, `--reverse` applies
after optional transformed-name selection, skipping, and limiting, and before
optional grouping. It preserves all existing modes when omitted and is rejected
outside batch mode. The implementation merge is
`f64c1052e70ccef308646a6322a90d1d0c5a6ae4`; governance-only Finalization is
open through draft Finalization PR #46.
Exceptionally large integer input remains a known non-blocking availability
observation because input size is not explicitly bounded. Prompt History
remains an immutable Engineering Platform record and is not copied into this
repository.
