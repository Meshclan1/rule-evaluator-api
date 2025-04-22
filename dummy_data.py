holdings = [
    {"isin": "US1234567890", "name": "Apple", "value": 15000000, "country": "US"},
    {"isin": "GB0987654321", "name": "BP", "value": 8000000, "country": "UK"},
    {"isin": "JP1122334455", "name": "Toyota", "value": 25000000, "country": "JP"},
]

rules = [
    {"type": "value_threshold", "threshold": 20000000},
    {"type": "country_blacklist", "countries": ["JP"]}
]

VALID_CURRENCIES = {"USD", "GBP", "EUR", "JPY"}
print(holdings)