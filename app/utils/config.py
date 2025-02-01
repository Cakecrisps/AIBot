import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DEBUG_MODE = os.getenv('DEBUG_MODE') == 'True'
PAYMENT_SYSTEM_URL = os.getenv('PAYMENT_SYSTEM_URL')
USER_FOLDER = os.getenv('USER_FOLDER')
DATABASE_URL = os.getenv('DATABASE_URL')
CHANNEL_ID = os.getenv('CHANNEL_ID')
CHANNEL_URL = os.getenv('CHANNEL_URL')
if DEBUG_MODE:
    TELEGRAM_TOKEN = os.getenv('TEST_TELEGRAM_TOKEN')
