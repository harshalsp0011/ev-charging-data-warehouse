import requests
import json
import time
import logging
from datetime import datetime
from pathlib import Path
import sys

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent.parent))
from config.api_config import NREL_API_KEY, NREL_BASE_URL, REQUEST_TIMEOUT, MAX_RETRIES, RATE_LIMIT_DELAY

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class NRELExtractor:
    def __init__(self):
        self.api_key = NREL_API_KEY
        self.base_url = NREL_BASE_URL
        self.session = requests.Session()
        
    def extract_stations(self, fuel_type="ELEC", state="CA", limit=50):
        """
        Extract EV charging stations from NREL API
        
        Args:
            fuel_type (str): Fuel type filter (ELEC for electric)
            state (str): State code filter
            limit (int): Maximum number of stations to retrieve
        """
        endpoint = f"{self.base_url}.json"
        
        params = {
            'api_key': self.api_key,
            'fuel_type': fuel_type,
            'state': state,
            'limit': limit,
            'format': 'json'
        }
        
        logger.info(f"Extracting NREL stations: fuel_type={fuel_type}, state={state}, limit={limit}")
        
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(
                    endpoint,
                    params=params,
                    timeout=REQUEST_TIMEOUT
                )
                response.raise_for_status()
                
                # Add delay for rate limiting
                time.sleep(RATE_LIMIT_DELAY)
                
                data = response.json()
                logger.info(f"Successfully extracted {len(data.get('fuel_stations', []))} stations")
                
                return data
                
            except requests.exceptions.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == MAX_RETRIES - 1:
                    logger.error(f"Failed to extract NREL data after {MAX_RETRIES} attempts")
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def save_to_file(self, data, filename=None):
        """Save extracted data to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"nrel_stations_{timestamp}.json"
        
        output_path = Path("data/raw") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Data saved to {output_path}")
        return output_path

def main():
    """Main extraction function"""
    try:
        extractor = NRELExtractor()
        
        # Extract stations for multiple states
        states = ["CA", "NY", "TX", "FL", "WA"]
        all_stations = []
        
        for state in states:
            logger.info(f"Processing state: {state}")
            data = extractor.extract_stations(state=state, limit=100)
            all_stations.extend(data.get('fuel_stations', []))
            time.sleep(RATE_LIMIT_DELAY)
        
        # Combine all data
        combined_data = {
            'metadata': {
                'extraction_date': datetime.now().isoformat(),
                'total_stations': len(all_stations),
                'states_processed': states
            },
            'fuel_stations': all_stations
        }
        
        # Save to file
        output_path = extractor.save_to_file(combined_data)
        logger.info(f"Extraction complete. {len(all_stations)} stations saved to {output_path}")
        
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise

if __name__ == "__main__":
    main()
