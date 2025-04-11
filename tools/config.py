import os
from dotenv import load_dotenv

load_dotenv()  

EMAIL_CONFIG = {
    "IMAP_SERVER": os.getenv("IMAP_SERVER"),
    "EMAIL": os.getenv("EMAIL_ADDRESS"),
    "PASSWORD": os.getenv("EMAIL_PASSWORD"),
    "SMTP_SERVER": os.getenv("SMTP_SERVER"),
    "SMTP_PORT": 587
}




OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 512))

