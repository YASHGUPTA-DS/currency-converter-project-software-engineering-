"""
converter.py
Core conversion logic. Kept separate from CLI/logging so it can be
tested on its own (this is why tests/test_converter.py can import it
directly without running main.py).
"""

import json
import os


class ConversionError(Exception):
    """Custom error for anything that goes wrong during conversion.
    main.py catches this and shows a friendly message instead of a
    raw Python traceback."""
    pass


def load_rates(rates_file="rates.json"):
    """Read exchange rates from a JSON config file.

    Rates are stored relative to a base currency (see rates.json).
    Example: if base is USD and INR: 95.24, that means 1 USD = 95.24 INR.
    """
    if not os.path.exists(rates_file):
        raise ConversionError(f"Rates file '{rates_file}' not found.")

    try:
        with open(rates_file, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ConversionError(f"Rates file '{rates_file}' is not valid JSON.")

    if "rates" not in data or "base_currency" not in data:
        raise ConversionError("Rates file is missing 'base_currency' or 'rates'.")

    return data["base_currency"], data["rates"]


def validate_currency_code(code, rates):
    """Check that a currency code exists in our rates dictionary."""
    if not isinstance(code, str):
        raise ConversionError(f"Currency code must be text, got: {code!r}")

    code = code.upper().strip()
    if code not in rates:
        supported = ", ".join(sorted(rates.keys()))
        raise ConversionError(
            f"Unsupported currency code '{code}'. Supported codes: {supported}"
        )
    return code


def validate_amount(amount):
    """Check that the amount is a valid positive number."""
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        raise ConversionError(f"Amount must be a number, got: {amount!r}")

    if amount < 0:
        raise ConversionError("Amount cannot be negative.")

    return amount


def convert(from_currency, to_currency, amount, rates):
    """
    Convert `amount` from `from_currency` to `to_currency` using the
    given rates dict (all rates relative to the same base currency).

    Formula:
      amount_in_base = amount / rate[from_currency]
      result = amount_in_base * rate[to_currency]
    """
    from_currency = validate_currency_code(from_currency, rates)
    to_currency = validate_currency_code(to_currency, rates)
    amount = validate_amount(amount)

    amount_in_base = amount / rates[from_currency]
    result = amount_in_base * rates[to_currency]

    return round(result, 2)
