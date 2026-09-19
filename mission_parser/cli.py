"""Initial parser candidate for the isolated Mission qualification target."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Read one name and quantity record")
    parser.add_argument("record")
    args = parser.parse_args()
    print(args.record)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
