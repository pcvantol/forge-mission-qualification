# Forge Mission qualification target

This private repository is an isolated, disposable target for one Forge
autonomous Mission qualification. It has no production data or credentials.

The installed `mission-parser` command initially echoes its argument. The
Mission goal is to reject malformed records with a stable error and emit
canonical JSON for valid `name:quantity` records. The independent consumer
tests in `acceptance/` install the package into fresh environments and invoke
the installed command. They deliberately fail on this baseline. The delivery
smoke suite in `tests/` is green, allowing a protected partial delivery while
the two independent behavioral controls remain separately observable.

This repository's protected `main` branch and review/check records are part
of the qualification evidence. No production Mission uses this repository.
