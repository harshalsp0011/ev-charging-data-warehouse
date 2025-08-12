#!/usr/bin/env python3
"""
NREL API Connection Test for EV Charging Data Warehouse
Tests API access and explores data structure for schema design
"""

import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# Load environment variables
load_dotenv()

def test_nrel_connection():
    """Test basic NREL API connection and data retrieval"""
    
    print("🔋 Testing NREL API Connection")
    print("=" * 50)
    
    api_key = os.getenv('NREL_API_KEY')
    if not api_key:
        print("❌ NREL_API_KEY not found in .env file")
        return False
    
    # Test API endpoint
    url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"
    params = {
        'api_key': api_key,
        'fuel_type': 'ELEC',  # Electric vehicles only
        'limit': 5,           # Small test sample
        'status': 'E'         # Currently operational
    }
    
    try:
        print(f"📡 Making API request to NREL...")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            stations = data.get('fuel_stations', [])
            
            print(f"✅ API Connection Successful!")
            print(f"📊 Retrieved {len(stations)} stations")
            print(f"🔍 Total stations available: {data.get('total_results', 'Unknown')}")
            
            return stations
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Connection Error: {str(e)}")
        return False

def explore_station_data(stations):
    """Analyze the structure and content of NREL station data"""
    
    if not stations:
        return
    
    print("\n🔍 Exploring Station Data Structure")
    print("-" * 40)
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame(stations)
    
    print(f"📈 Data Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"📋 Available Fields: {len(df.columns)} total")
    
    # Show key field information
    print("\n📊 Key EV Charging Fields:")
    key_fields = [
        'station_name', 'city', 'state', 'latitude', 'longitude',
        'ev_level1_evse_num', 'ev_level2_evse_num', 'ev_dc_fast_num',
        'ev_network', 'ev_connector_types', 'access_code'
    ]
    
    for field in key_fields:
        if field in df.columns:
            non_null = df[field].notna().sum()
            print(f"  ✅ {field:<20}: {non_null}/{len(df)} records have data")
        else:
            print(f"  ❌ {field:<20}: Field not found")
    
    # Sample station details
    print("\n🏢 Sample Station Details:")
    sample_station = stations[0]
    print(f"  Station: {sample_station.get('station_name', 'N/A')}")
    print(f"  Location: {sample_station.get('city', 'N/A')}, {sample_station.get('state', 'N/A')}")
    print(f"  Network: {sample_station.get('ev_network', 'N/A')}")
    print(f"  Level 2 Ports: {sample_station.get('ev_level2_evse_num', 0)}")
    print(f"  DC Fast Ports: {sample_station.get('ev_dc_fast_num', 0)}")
    
    return df

def test_geographic_filtering():
    """Test geographic filtering capabilities"""
    
    print("\n🗺️  Testing Geographic Filtering")
    print("-" * 40)
    
    api_key = os.getenv('NREL_API_KEY')
    url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"
    
    # Test California stations
    params = {
        'api_key': api_key,
        'fuel_type': 'ELEC',
        'state': 'CA',
        'limit': 10
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            ca_count = data.get('total_results', 0)
            print(f"🏖️  California EV Stations: {ca_count:,}")
        
        # Test DC fast charging stations
        params['ev_charging_level'] = 'dc_fast'
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            dc_fast_count = data.get('total_results', 0)
            print(f"⚡ CA DC Fast Chargers: {dc_fast_count:,}")
            
    except Exception as e:
        print(f"❌ Geographic test error: {e}")

def save_sample_data(stations):
    """Save sample data for schema design reference"""
    
    print("\n💾 Saving Sample Data")
    print("-" * 40)
    
    try:
        # Save raw JSON sample
        with open('sample_nrel_data.json', 'w') as f:
            json.dump(stations[:3], f, indent=2)
        
        # Save as CSV for analysis
        df = pd.DataFrame(stations)
        df.to_csv('sample_nrel_stations.csv', index=False)
        
        print("✅ Sample data saved:")
        print("  📄 sample_nrel_data.json (3 stations, full detail)")
        print("  📊 sample_nrel_stations.csv (all test stations)")
        
    except Exception as e:
        print(f"❌ Save error: {e}")

def main():
    """Run all NREL API tests"""
    
    print("🔋 NREL API Connection Test")
    print("=" * 60)
    print(f"⏰ Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test basic connection
    stations = test_nrel_connection()
    
    if stations:
        # Explore data structure
        df = explore_station_data(stations)
        
        # Test geographic filtering
        test_geographic_filtering()
        
        # Save sample data
        save_sample_data(stations)
        
        print("\n🎉 NREL API Testing Complete!")
        print("✅ Ready to proceed to weather API testing")
    else:
        print("\n❌ NREL API testing failed")
        print("Please check your API key and internet connection")

if __name__ == "__main__":
    main()
