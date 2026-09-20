"""Command-line parser for the isolated Mission qualification target."""
from __future__ import annotations

import argparse
import json
import sys


def _positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def _non_negative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be a non-negative integer")
    return number


def _parse_record(record: str) -> dict[str, str | int]:
    name, quantity_text = record.split(":")
    if not name or not quantity_text:
        raise ValueError

    quantity = int(quantity_text)
    if quantity <= 0:
        raise ValueError

    return {"name": name, "quantity": quantity}


def _parse_and_scale_batch(
    records: str, *, scale: int, prefix: str
) -> tuple[list[dict[str, str | int]], int | None]:
    items = []
    for index, record in enumerate(records.split(","), start=1):
        try:
            item = _parse_record(record)
        except ValueError:
            return [], index

        item["quantity"] *= scale
        item["name"] = prefix + item["name"]
        items.append(item)

    return items, None


def _select_and_limit_batch(
    items: list[dict[str, str | int]],
    *,
    selected_name: str | None,
    limit: int | None,
    skip: int | None = None,
) -> list[dict[str, str | int]]:
    if selected_name is not None:
        items = [item for item in items if item["name"] == selected_name]
    if skip:
        items = items[skip:]
    if limit is not None:
        items = items[:limit]
    return items


def _group_batch(
    items: list[dict[str, str | int]],
) -> list[dict[str, str | int]]:
    grouped_items = {}
    for item in items:
        name = item["name"]
        grouped_items[name] = grouped_items.get(name, 0) + item["quantity"]
    return [
        {"name": name, "quantity": quantity}
        for name, quantity in grouped_items.items()
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Read name and quantity records")
    parser.add_argument("--batch", action="store_true")
    parser.add_argument("--group", action="store_true")
    parser.add_argument("--select")
    parser.add_argument("--skip", type=_non_negative_int)
    parser.add_argument("--limit", type=_positive_int)
    parser.add_argument("--prefix", default="")
    parser.add_argument("--scale", type=_positive_int, default=1)
    parser.add_argument("record")
    args = parser.parse_args()

    if args.group and not args.batch:
        parser.error("--group requires --batch")
    if args.select is not None and not args.batch:
        parser.error("--select requires --batch")
    if args.skip is not None and not args.batch:
        parser.error("--skip requires --batch")
    if args.limit is not None and not args.batch:
        parser.error("--limit requires --batch")

    if args.batch:
        items, invalid_index = _parse_and_scale_batch(
            args.record, scale=args.scale, prefix=args.prefix
        )
        if invalid_index is not None:
            print(f"invalid batch record at index {invalid_index}", file=sys.stderr)
            return 1

        items = _select_and_limit_batch(
            items, selected_name=args.select, skip=args.skip, limit=args.limit
        )

        if args.group:
            items = _group_batch(items)

        result = {
            "items": items,
            "total_quantity": sum(item["quantity"] for item in items),
        }
        print(json.dumps(result, separators=(",", ":")))
        return 0

    try:
        result = _parse_record(args.record)
    except ValueError:
        print("invalid record", file=sys.stderr)
        return 1

    result["quantity"] *= args.scale
    result["name"] = args.prefix + result["name"]
    print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
