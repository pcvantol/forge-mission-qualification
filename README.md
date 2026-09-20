# Forge Mission qualification target

This repository is an isolated, disposable target for one Forge
autonomous Mission qualification. It has no production data or credentials.

The installed `mission-parser` command rejects malformed records with a stable
error and emits canonical JSON for valid `name:quantity` records. The
independent consumer tests in `acceptance/` install the package into fresh
environments and invoke the installed command. The delivery smoke suite lives
in `tests/`, while the behavioral controls remain separately observable.

The two approved observation selectors are
`acceptance.test_invalid_record` and `acceptance.test_valid_record`. Each
records one behavioral criterion separately on the delivered revision.

This repository's protected `main` branch and review/check records are part
of the qualification evidence. No production Mission uses this repository.

## Delivered qualification objective

The installed command requires positive quantities for single records while
preserving the existing canonical output for valid records.

Installed `--batch` mode accepts comma-separated `name:quantity` records and
emits one canonical JSON object with ordered
`items` and `total_quantity`. An invalid element rejects the entire batch with
`invalid batch record at index N` on stderr (one-based index), exit code 1,
and no partial stdout. The separately observed controls are
`acceptance.test_positive_record` and `acceptance.test_batch_records`.
They pass on the delivered implementation.

The `--scale` option accepts a positive integer and multiplies quantities in
both single-record and batch modes. Batch totals are calculated from the scaled
quantities. Omitting the option retains the prior output, and a non-positive
scale is rejected without emitting a result. The independent control is
`acceptance.test_scaled_quantity`.

In batch mode, `--group` combines repeated names after scaling while preserving
first-seen order. Omitting `--group` preserves ordered, ungrouped output, and
single-record mode remains unchanged. The independent control is
`acceptance.grouped_batch_contract`. Because that module does not use the
default `test*.py` discovery name, run the complete acceptance surface with
`python3 -m unittest discover -s acceptance -t . -p '*.py'`.

In batch mode, `--select` retains records whose transformed name exactly
matches its value after optional prefixing. Matching records preserve input
order; selection occurs before optional grouping and totals are recomputed from
the selected records. `--select` is rejected outside batch mode. The
independent control is `acceptance.selected_batch_contract`.

A positive batch `--limit` is applied after selection and before grouping,
preserving the selected records' input order. Omitting `--limit` preserves the
existing output, and the option is rejected outside batch mode. The independent
control is `acceptance.limited_selected_batch_contract`.

In batch mode, non-negative `--skip` is applied after optional selection and
before optional limiting and grouping. Retained records preserve their input
order, zero leaves the selected records unchanged, and negative values are
rejected. `--skip` is rejected outside batch mode. The independent control is
`acceptance.skipped_batch_contract`.

Implementation PR #61 is merged on protected `main` for run
`inbox-8c39cd5b65e84824a05d5ed97cdadc76`. The implementation merge is
`ea594372bbc0973078836b39ade97e6440cd2f50`; governance-only Finalization is
being prepared on the run's bounded Finalization branch. The implementation diff is
confined to `mission_parser/cli.py`
and does not implement `--reverse`. Any future `--reverse` objective must be
derived again from accepted terminal delivery evidence and this reconciled repository truth.
Exceptionally large integer input remains a known non-blocking availability
observation because input size is not explicitly bounded. The run's Prompt
History remains immutable in the Engineering Platform.
