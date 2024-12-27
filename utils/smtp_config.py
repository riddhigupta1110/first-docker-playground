import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SMTP configuration settings
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USE_TLS = os.getenv("SMTP_USE_TLS", "False") == "true"  # Convert to boolean
SMTP_USE_SSL = os.getenv("SMTP_USE_SSL", "True") == "True"  # Convert to boolean
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_DEFAULT_SENDER = os.getenv("SMTP_DEFAULT_SENDER")

def get_smtp_config():
    # print("SMTP_SERVER:", SMTP_SERVER)
    # print("SMTP_PORT:", SMTP_PORT)
    # print("SMTP_USE_TLS:", SMTP_USE_TLS)
    # print("SMTP_USE_SSL:", SMTP_USE_SSL)
    # print("SMTP_USER:", SMTP_USER)
    # print("SMTP_PASSWORD:", SMTP_PASSWORD)
    # print("SMTP_DEFAULT_SENDER:", SMTP_DEFAULT_SENDER)
    
    return {
        "MAIL_SERVER": SMTP_SERVER,
        "MAIL_PORT": SMTP_PORT,
        "MAIL_USE_TLS": SMTP_USE_TLS,
        "MAIL_USE_SSL": SMTP_USE_SSL,
        "MAIL_USERNAME": SMTP_USER,
        "MAIL_PASSWORD": SMTP_PASSWORD,
        "MAIL_DEFAULT_SENDER": SMTP_DEFAULT_SENDER
    }
