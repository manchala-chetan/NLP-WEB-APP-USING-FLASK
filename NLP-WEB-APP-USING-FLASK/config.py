import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Get the current directory (where app.py is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key-change-in-production')

    # API keys
    PARALLELDOTS_API_KEY = os.environ.get('PARALLELDOTS_API_KEY', '')

    # Database configuration
    # Use the users.json file in the parent directory
    DB_FILENAME = os.environ.get('DB_FILENAME', os.path.join(PARENT_DIR, 'users.json'))
