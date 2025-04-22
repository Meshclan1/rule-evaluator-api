from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("TEST")
print(database_url)

# This is a test file to ensure things are working!
# if len(database_url) != 7 or database_url[0:7] != "sqlite:":
#    print("database url is not valid")
#else:
#    print("database url is valid")
#    print("This is a test file to ensure things are working!")
    
    