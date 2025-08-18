import requests
import json
import time
import logging
from datetime import datetime
from pathlib import Path
import sys

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent.parent))
from config.api_config import OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL, REQUEST_TIMEOUT, MAX_RETRIES, RATE_LIMIT_DELAY

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WeatherExtractor:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY
        self.base_url = OPENWEATHER_BASE_URL
        self.session = requests.Session()
    
    def extract_current_weather(self, cities):
        """
        Extract current weather for specified cities
        
        Args:
            cities (list): List of city names or coordinates
        """
        weather_data = []
        
        for city in cities:
            logger.info(f"Extracting weather for: {city}")
            
            endpoint = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Celsius
            }
            
            for attempt in range(MAX_RETRIES):
                try:
                    response = self.session.get(
                        endpoint,
                        params=params,
                        timeout=REQUEST_TIMEOUT
                    )
                    response.raise_for_status()
                    
                    data = response.json()
                    data['extraction_timestamp'] = datetime.now().isoformat()
                    weather_data.append(data)
                    
                    logger.info(f"Successfully extracted weather for {city}")
                    time.sleep(RATE_LIMIT_DELAY)
                    break
                    
                except requests.exceptions.RequestException as e:
                    logger.warning(f"Attempt {attempt + 1} failed for {city}: {e}")
                    if attempt == MAX_RETRIES - 1:
                        logger.error(f"Failed to extract weather for {city}")
                    else:
                        time.sleep(2 ** attempt)
        
        return weather_data
    
    def save_to_file(self, data, filename=None):
        """Save extracted data to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"weather_data_{timestamp}.json"
        
        output_path = Path("data/raw") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Weather data saved to {output_path}")
        return output_path

def main():
    """Main extraction function"""
    try:
        extractor = WeatherExtractor()
        
        # Major cities for weather data
        cities = [
            "Los Angeles,CA,US",
            "New York,NY,US", 
            "Chicago,IL,US",
            "Houston,TX,US",
            "Phoenix,AZ,US",
            "Philadelphia,PA,US",
            "San Antonio,TX,US",
            "San Diego,CA,US",
            "Dallas,TX,US",
            "Austin,TX,US"
        ]
        
        # Extract weather data
        weather_data = extractor.extract_current_weather(cities)
        
        # Combine with metadata
        combined_data = {
            'metadata': {
                'extraction_date': datetime.now().isoformat(),
                'total_cities': len(cities),
                'successful_extractions': len(weather_data)
            },
            'weather_data': weather_data
        }
        
        # Save to file
        output_path = extractor.save_to_file(combined_data)
        logger.info(f"Weather extraction complete. {len(weather_data)} cities saved to {output_path}")
        
    except Exception as e:
        logger.error(f"Weather extraction failed: {e}")
        raise

if __name__ == "__main__":
    main()
