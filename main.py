"""Tiny a + b program.

Usage:
  python main.py 1 2        # prints 3
  python main.py 1.5 2.3    # prints 3.8
  python main.py            # prompts for a and b
"""

from __future__ import annotations
import argparse
import sys


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def parse_args(argv=None):
    """Parse optional positional arguments a and b."""
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", nargs="?", help="first number (int or float)", default=None)
    parser.add_argument("b", nargs="?", help="second number (int or float)", default=None)
    return parser.parse_args(argv)


def to_number(value: str) -> float:
    """Convert a string to float, raising ValueError on failure."""
    try:
        return float(value)
    except Exception as exc:
        raise ValueError(f"Invalid number: {value!r}") from exc


def main(argv=None) -> float:
    """CLI entry point: parse inputs, compute sum, print result, and return the value."""
    args = parse_args(argv)

    a_input = args.a
    b_input = args.b

    if a_input is None or b_input is None:
        try:
            a_input = input("a: ")
            b_input = input("b: ")
        except EOFError:
            print("No input provided", file=sys.stderr)
            sys.exit(1)

    try:
        a = to_number(a_input)
        b = to_number(b_input)
    except ValueError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    result = add(a, b)

    # Print as integer when the result has no fractional part.
    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)

    return result


if __name__ == "__main__":
    main()
