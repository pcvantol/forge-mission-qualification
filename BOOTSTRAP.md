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
modes. Installed batch mode can additionally select, skip, limit, and group
records, while single-mode and unchanged-option behavior remain intact.
Malformed records, non-positive quantities, and non-positive scales remain
rejected.

Protected `main` includes batch skipping through implementation PR #58 for run
`inbox-044602b879d14e7b9719df78f6111bed`. In batch mode, non-negative `--skip`
applies after optional transformed-name selection and before optional limiting
and grouping. Zero preserves the selected records, negative values are rejected,
and the option is rejected outside batch mode. The implementation merge is
`3909094fed1e2edc23cfae30ab0f9cceccc7c1bf`; governance-only Finalization is
open as draft PR #59 on the run's bounded Finalization branch.
Any future `--reverse` objective must be derived again from accepted terminal
delivery evidence and this reconciled repository truth.
Exceptionally large integer input remains a known non-blocking availability
observation because input size is not explicitly bounded. Prompt History
remains an immutable Engineering Platform record and is not copied into this
repository.
