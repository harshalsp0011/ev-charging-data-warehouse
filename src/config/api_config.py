import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
NREL_API_KEY = os.getenv('NREL_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

# API Endpoints
NREL_BASE_URL = "https://developer.nrel.gov/api/alt-fuel-stations/v1"
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

# Request settings
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RATE_LIMIT_DELAY = 1.0  # seconds between requests
# Headers for API requests