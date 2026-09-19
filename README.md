# Forge Mission qualification target

This repository is an isolated, disposable target for one Forge
autonomous Mission qualification. It has no production data or credentials.

The installed `mission-parser` command initially echoes its argument. The
Mission goal is to reject malformed records with a stable error and emit
canonical JSON for valid `name:quantity` records. The independent consumer
tests in `acceptance/` install the package into fresh environments and invoke
the installed command. They deliberately fail on this baseline. The delivery
smoke suite in `tests/` is green, allowing a protected partial delivery while
the two independent behavioral controls remain separately observable.

The two approved observation selectors are
`acceptance.test_invalid_record` and `acceptance.test_valid_record`. Each
records one behavioral criterion separately on the delivered revision; a
failed selector stays unproven while the ordinary delivery smoke gate can
still pass.

This repository's protected `main` branch and review/check records are part
of the qualification evidence. No production Mission uses this repository.

## Next bounded qualification objective

The installed command currently accepts zero and negative quantities. The next
behavioral objective requires positive quantities for single records, while
preserving the existing canonical output for valid records.

The same objective adds an installed `--batch` mode. Given comma-separated
`name:quantity` records, it emits one canonical JSON object with ordered
`items` and `total_quantity`. An invalid element rejects the entire batch with
`invalid batch record at index N` on stderr (one-based index), exit code 1,
and no partial stdout. The separately observed controls are
`acceptance.test_positive_record` and `acceptance.test_batch_records`.
They fail on the current implementation. The existing delivery smoke check
continues to pass, allowing genuine partial progress to be observed without
altering a failing control.
