# Forge Mission qualification target

This repository is an isolated, disposable target for one Forge
autonomous Mission qualification. It has no production data or credentials.

The installed `mission-parser` command rejects malformed records with a stable
error and emits canonical JSON for valid `name:quantity` records. The
independent consumer tests in `acceptance/` install the package into fresh
environments and invoke the installed command. The delivery smoke suite in
`tests/` and both independent behavioral controls are green on the delivered
revision.

The two approved observation selectors are
`acceptance.test_invalid_record` and `acceptance.test_valid_record`. Each
records one behavioral criterion separately on the delivered revision; a
failed selector stays unproven while the ordinary delivery smoke gate can
still pass.

This repository's protected `main` branch and review/check records are part
of the qualification evidence. No production Mission uses this repository.

Implementation pull request #3 delivered the parser behavior. The subsequent
Finalization pull request is limited to sanitized governance and handoff
records.
