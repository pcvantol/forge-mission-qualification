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

Implementation PR #18 is merged on protected `main`. The governance-only
Finalization for run `inbox-5fa3148502e64093aca6b00c52651211` is pending in
draft Finalization PR #19. Its Prompt History remains immutable in the
Engineering Platform.
