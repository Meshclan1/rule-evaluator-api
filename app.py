from dotenv import load_dotenv
import os
from holdings import Holding, VALID_CURRENCIES 


new_holding = Holding(
    isin="US0378331005",  # 12 characters as required
    name="Apple Inc",
    value=150.75,         # Positive value as required
    currency="USD"        # Must be one of the VALID_CURRENCIES
)
print(new_holding)
print(VALID_CURRENCIES)

load_dotenv()

database_url = os.getenv("TEST")
print(database_url)

# This is a test file to ensure things are working!
# if len(database_url) != 7 or database_url[0:7] != "sqlite:":
#    print("database url is not valid")
#else:
#    print("database url is valid")
#    print("This is a test file to ensure things are working!")
    
    