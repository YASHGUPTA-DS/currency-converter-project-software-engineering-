CURRENCY CONVERTER - Systems Product (Part 2)
================================================

WHAT THIS IS
------------
A command-line currency converter that reads exchange rates from a
config file (rates.json), validates user input, logs every action,
and never crashes on bad input.


REQUIREMENTS
------------
- Python 3.7 or higher
- No external packages needed (see requirements.txt)


FOLDER STRUCTURE
-----------------
main.py             -> CLI entry point (run this)
src/converter.py     -> conversion logic + input validation
src/logger.py        -> logging setup
rates.json           -> exchange rate configuration
tests/test_converter.py -> automated unit tests
app.log              -> auto-created log file (created on first run)


INSTALLATION
------------
1. Make sure Python 3 is installed:
       python3 --version

2. No pip installs needed. Just navigate into this folder:
       cd Part2_SystemsProduct


USAGE
-----
Run a conversion like this:

    python main.py --from USD --to EUR --amount 150

Arguments:
    --from      Currency code to convert FROM (e.g. USD)
    --to        Currency code to convert TO (e.g. EUR)
    --amount    Amount to convert (must be a positive number)

Example output:
    150 USD = 138.0 EUR


CONFIGURING EXCHANGE RATES (rates.json)
-----------------------------------------
Rates are stored relative to a base currency. Example:

    {
      "base_currency": "USD",
      "rates": {
        "USD": 1.0,
        "INR": 95.24,
        "EUR": 0.92
      }
    }

This means 1 USD = 95.24 INR, and 1 USD = 0.92 EUR.
To add a new currency, just add a new "CODE": rate line to rates.json.

(Note: to use a LIVE API instead of rates.json, you would replace the
load_rates() function in src/converter.py with a call to an API like
ExchangeRate-API, and pass the returned rates dict to convert() the
same way.)


ERROR HANDLING
----------------
The program handles bad input gracefully and never shows a raw
Python traceback. Examples:

    python main.py --from USD --to XYZ --amount 150
    -> Error: Unsupported currency code 'XYZ'. Supported codes: ...

    python main.py --from USD --to EUR --amount -50
    -> Error: Amount cannot be negative.

    python main.py --from USD --to EUR --amount abc
    -> Error: Amount must be a number, got: 'abc'

All actions (success or failure) are logged with a timestamp to
app.log.


RUNNING TESTS
--------------
From inside the Part2_SystemsProduct folder, run:

    python -m unittest tests/test_converter.py -v

This runs 10 tests covering:
    - normal ("happy path") conversions
    - negative amounts
    - non-numeric amounts
    - unsupported currency codes
    - zero amount (valid edge case)
    - lowercase currency codes


AUTHOR NOTES
------------
This is Part 2 of a two-part assignment. Part 1 (Part1_Program/) is
a simple hardcoded script with no error handling, built to contrast
with this production-style version.
