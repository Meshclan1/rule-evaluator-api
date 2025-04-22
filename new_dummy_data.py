holdings = [
    {"isin": "US1234567890", "name": "Apple", "value": 15000000, "currency": "USD"},
    {"isin": "GB0987654321", "name": "BP", "value": 8000000, "currency": "GBP"},
    {"isin": "JP1122334455", "name": "Toyota", "value": 25000000, "currency": "JPY"},
    ] 

rules = [
    {"type": "value_threshold", "threshold": 20000000},
    {"type": "currency_blacklist", "currencies": ["JPY"]}
]

print(holdings)