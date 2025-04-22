# Build an API endpoint that clients can reach and submit their holdings data as a JSON payload. 
# The endpoint should evaluate each incoming holding against defined rules
# If there are violations, then return a list of these violations

#Pseudo code:
# for each holding:
#    for each rule:
#        if the holding violates the rule:
#            add to violations list


# ✅ Rules:
#    isin must be a 12-character string
#    value must be a positive number
#    currency must be one of: ["USD", "GBP", "EUR", "JPY"]

from pydantic import BaseModel, Field, field_validator

# validation rules


VALID_CURRENCIES = {"USD", "GBP", "EUR", "JPY"}

class Holding(BaseModel):
    isin: str = Field(..., min_length=12, max_length=12)
    name: str
    value: float
    currency: str

    @field_validator('value')
    def value_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Value must be positive")
        return v

    @field_validator('currency')
    def currency_must_be_valid(cls, v):
        if v not in VALID_CURRENCIES:
            raise ValueError(f"Currency must be one of {VALID_CURRENCIES}")
        return v


workplace = [
    {"isin": "US1234567890", "name": "Apple", "value": 15000000, "currency": "USD"},
    {"isin": "GB0987654321", "name": "BP", "value": 8000000, "currency": "GBP"},
    {"isin": "JP1122334455", "name": "Toyota", "value": 25000000, "currency": "JPY"},
]




def check_compliance(holdings, rules):
    violations = []

    for holding in holdings:
        for rule in rules:
            if rule['type'] == 'value_threshold':
                if holding['value'] > rule['threshold']:
                    violations.append({
                        'isin': holding['isin'],
                        'rule': 'value_threshold'
                    })
            elif rule['type'] == 'country_blacklist':
                if holding['country'] in rule['countries']:
                    violations.append({
                        'isin': holding['isin'],
                        'rule': 'country_blacklist'
                    })
    
    return violations


