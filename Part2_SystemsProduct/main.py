"""
main.py
CLI entry point.

Usage:
    python main.py --from USD --to EUR --amount 150
"""
import __main__
import argparse
import sys
import os

# Let Python find src/ folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from converter import load_rates, convert, ConversionError
from logger import get_logger

RATES_FILE = os.path.join(os.path.dirname(__file__), "rates.json")


def main():
    logger = get_logger()

    parser = argparse.ArgumentParser(description="Convert an amount between currencies.")
    parser.add_argument("--from", dest="from_currency", required=True, help="Currency code to convert FROM (e.g. USD)")
    parser.add_argument("--to", dest="to_currency", required=True, help="Currency code to convert TO (e.g. EUR)")
    parser.add_argument("--amount", dest="amount", required=True, help="Amount to convert")

    args = parser.parse_args()

    try:
        base_currency, rates = load_rates(RATES_FILE)
        result = convert(args.from_currency, args.to_currency, args.amount, rates)

        message = f"{args.amount} {args.from_currency.upper()} = {result} {args.to_currency.upper()}"
        print(message)
        logger.info(f"SUCCESS: {message}")

    except ConversionError as e:
        # This is OUR expected error type -> friendly message, no traceback
        print(f"Error: {e}")
        logger.error(f"FAILED: {e}")
        sys.exit(1)

    except Exception as e:
        # Catch-all safety net so the program NEVER crashes with a raw traceback
        print(f"Unexpected error occurred. Please check your input and try again.")
        logger.error(f"UNEXPECTED ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
