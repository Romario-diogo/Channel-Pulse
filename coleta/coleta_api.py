
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("KEYS_YOUTUBE")
print(key)