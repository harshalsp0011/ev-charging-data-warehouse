#!/usr/bin/env python3
"""
OpenWeatherMap API Connection Test
Tests API access and explores weather data structure for EV project
"""

import requests
import os
from dotenv import load_dotenv
import pandas as pd
import json
from datetime import datetime

# Load environment variables
load_dotenv()

def test_weather_connection():
    print("☁️ Testing OpenWeatherMap API Connection")
    print("=" * 50)

    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print("❌ OPENWEATHER_API_KEY not found in .env")
        return False

    # Sample locations
    locations = [
        {"city": "San Francisco", "lat": 37.7749, "lon": -122.4194},
        {"city": "New York", "lat": 40.7128, "lon": -74.0060},
        {"city": "Chicago", "lat": 41.8781, "lon": -87.6298}
    ]

    results = []
    for loc in locations:
        params = {
            "lat": loc["lat"],
            "lon": loc["lon"],
            "appid": api_key,
            "units": "metric"
        }
        try:
            print(f"📡 Requesting weather for {loc['city']}...")
            response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params=params,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Retrieved data for {loc['city']}")
                results.append({
                    "city": loc["city"],
                    "data": data
                })
            else:
                print(f"❌ Error {response.status_code} for {loc['city']}: {response.text}")
        except Exception as e:
            print(f"❌ Request error for {loc['city']}: {e}")

    return results

def explore_weather_data(results):
    if not results:
        return

    print("\n🔍 Exploring Weather Data Structure")
    print("-" * 50)

    # Flatten JSON for DataFrame
    records = []
    for item in results:
        d = item["data"]
        record = {
            "city": item["city"],
            "temp": d["main"]["temp"],
            "feels_like": d["main"]["feels_like"],
            "humidity": d["main"]["humidity"],
            "pressure": d["main"]["pressure"],
            "weather_main": d["weather"][0]["main"],
            "weather_desc": d["weather"][0]["description"],
            "wind_speed": d["wind"]["speed"],
            "clouds_all": d.get("clouds", {}).get("all", None)
        }
        records.append(record)

    df = pd.DataFrame(records)
    print(f"📈 DataFrame shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\n📊 Available Fields and Sample Values:")
    print(df.head().to_string(index=False))

    return df

def save_sample_weather(df):
    if df is None or df.empty:
        return

    print("\n💾 Saving Sample Weather Data")
    print("-" * 50)
    # Save JSON
    with open("sample_weather_data.json", "w") as f:
        json.dump([r["data"] for r in results], f, indent=2)

    # Save CSV
    df.to_csv("sample_weather_data.csv", index=False)
    print("✅ Saved sample_weather_data.json and sample_weather_data.csv")

if __name__ == "__main__":
    print(f"⏰ Test Time: {datetime.now()}")
    results = test_weather_connection()
    df = explore_weather_data(results)
    save_sample_weather(df)
