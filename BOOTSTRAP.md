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

Protected `main` includes non-negative batch skipping through implementation PR
#42 for run `inbox-52c2e7c0bd6a43e58d5a88bd2ba503d7`. In batch mode, `--skip`
applies after optional transformed-name selection and before optional limiting
and grouping. Input order is preserved, zero leaves the selected records
unchanged, negative values and non-batch use are rejected, and `--reverse` is
not implemented. Governance-only Finalization is merged through Finalization
PR #43. The implementation merge is
`b4f1276213b6ddbeaaeb9f1cc1b03775221649b1`, and the Finalization merge is
`4a3539c46816b0ae1efdb1c0609ad97147129f0e`.
Exceptionally large integer input remains a known non-blocking availability
observation because input size is not explicitly bounded. Prompt History
remains an immutable Engineering Platform record and is not copied into this
repository.
