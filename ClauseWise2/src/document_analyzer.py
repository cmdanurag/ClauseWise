import os
from pathlib import Path
from dotenv import load_dotenv

# Force load .env and override existing environment variables
load_dotenv(override=True)

# Load Google credentials path from .env
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not cred_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set in .env")

# Normalize Windows path
GOOGLE_CREDENTIALS_PATH = Path(cred_path.strip())

# Check that the file exists
if not GOOGLE_CREDENTIALS_PATH.exists():
    raise FileNotFoundError(
        f"Google credentials file not found at: {GOOGLE_CREDENTIALS_PATH}\n"
        "Please check your .env and ensure the file exists."
    )

# Set the environment variable for Google libraries
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(GOOGLE_CREDENTIALS_PATH)

print("Using Google credentials:", GOOGLE_CREDENTIALS_PATH)
