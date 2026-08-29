"""
Part 1: The Program
A quick, simple script — no error handling, no CLI, no API.
Just hardcoded expenses in INR converted to USD.
"""

# Fixed exchange rate: 1 USD = 95.24 INR
EXCHANGE_RATE_INR_TO_USD = 95.24

# Hardcoded list of expenses in INR
expenses_inr = [500, 1200, 3000, 750, 15000]

print("Expense Report: INR -> USD")
print("-" * 35)

for expense in expenses_inr:
    usd_amount = expense / EXCHANGE_RATE_INR_TO_USD
    print(f"INR {expense:>8.2f}  ->  USD {usd_amount:.2f}")

total_inr = sum(expenses_inr)
total_usd = total_inr / EXCHANGE_RATE_INR_TO_USD

print("-" * 35)
print(f"Total INR: {total_inr:.2f}")
print(f"Total USD: {total_usd:.2f}")
