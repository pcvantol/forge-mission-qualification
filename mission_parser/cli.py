"""Command-line parser for the isolated Mission qualification target."""
from __future__ import annotations

import argparse
import json
import sys


def _parse_record(record: str) -> dict[str, str | int]:
    name, quantity_text = record.split(":")
    if not name or not quantity_text:
        raise ValueError

    quantity = int(quantity_text)
    if quantity <= 0:
        raise ValueError

    return {"name": name, "quantity": quantity}


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def _scale_record(record: dict[str, str | int], scale: int) -> dict[str, str | int]:
    return {"name": record["name"], "quantity": record["quantity"] * scale}


def _group_records(records: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    quantities: dict[str, int] = {}
    for record in records:
        name = str(record["name"])
        quantities[name] = quantities.get(name, 0) + int(record["quantity"])
    return [{"name": name, "quantity": quantity} for name, quantity in quantities.items()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Read name and quantity records")
    parser.add_argument("--batch", action="store_true")
    parser.add_argument("--group", action="store_true")
    parser.add_argument("--scale", type=_positive_int, default=1)
    parser.add_argument("record")
    args = parser.parse_args()

    if args.group and not args.batch:
        parser.error("--group requires --batch")

    if args.batch:
        items = []
        for index, record in enumerate(args.record.split(","), start=1):
            try:
                items.append(_scale_record(_parse_record(record), args.scale))
            except ValueError:
                print(f"invalid batch record at index {index}", file=sys.stderr)
                return 1

        if args.group:
            items = _group_records(items)

        result = {
            "items": items,
            "total_quantity": sum(item["quantity"] for item in items),
        }
        print(json.dumps(result, separators=(",", ":")))
        return 0

    try:
        result = _scale_record(_parse_record(args.record), args.scale)
    except ValueError:
        print("invalid record", file=sys.stderr)
        return 1

    print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
