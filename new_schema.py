from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import List
from new_dummy_data import holdings

VALID_CURRENCIES = {"USD", "GBP", "EUR", "JPY"}

class Holding(BaseModel):
    isin: str = Field(..., min_length=12, max_length=12)
    name: str
    value: float
    currency: str

    @field_validator('value')
    @classmethod
    def value_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Value must be positive")
        return v

    @field_validator('currency')
    @classmethod
    def currency_must_be_valid(cls, v):
        if v not in VALID_CURRENCIES:
            raise ValueError(f"Currency must be one of {VALID_CURRENCIES}")
        return v

class PortfolioUpload(BaseModel):
    holdingingo: List[Holding]
    

try:
    portfolio = PortfolioUpload(holdingingo=holdings)
    print(portfolio)
    print("✅ All holding values are valid!")
except ValidationError as e:
    print("❌ Errors found:")
    print(e)
