"""Command-line parser for the isolated Mission qualification target."""
from __future__ import annotations

import argparse
import json
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Read one name and quantity record")
    parser.add_argument("record")
    args = parser.parse_args()

    try:
        name, quantity_text = args.record.split(":")
        if not name or not quantity_text:
            raise ValueError
        quantity = int(quantity_text)
    except ValueError:
        print("invalid record", file=sys.stderr)
        return 1

    print(json.dumps({"name": name, "quantity": quantity}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
