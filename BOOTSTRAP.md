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

Protected `main` includes batch reversal through implementation PR #64 for run
`inbox-e173300d7dac4a8c998d1c788cc6782c`. In batch mode, `--reverse` applies
after optional transformed-name selection, skipping, and limiting, and before
optional grouping. Omitting the option preserves retained-record order, and the
option is rejected outside batch mode. The implementation merge is
`008719652f4b55c47136e5ec792a906ee2826b81`.
Exceptionally large integer input remains a known non-blocking availability
observation because input size is not explicitly bounded. Prompt History
remains an immutable Engineering Platform record and is not copied into this
repository.
