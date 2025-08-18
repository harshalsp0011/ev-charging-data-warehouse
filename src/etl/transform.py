import csv
import json
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(exist_ok=True)

def transform_ev_sessions(raw_csv, output_csv):
    """Normalize EV sessions CSV for staging."""
    with open(raw_csv, newline='') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = [
            "User ID", "Vehicle Model", "Battery Capacity (kWh)",
            "Charging Station ID", "Charging Station Location",
            "Charging Start Time", "Charging End Time",
            "Energy Consumed (kWh)", "Charging Duration (hours)",
            "Charging Rate (kW)", "Charging Cost (USD)",
            "Time of Day", "Day of Week",
            "State of Charge (Start %)", "State of Charge (End %)",
            "Distance Driven (since last charge) (km)",
            "Temperature (°C)", "Vehicle Age (years)",
            "Charger Type", "User Type"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            # Ensure timestamps are ISO format
            row["Charging Start Time"] = datetime.fromisoformat(row["Charging Start Time"]).isoformat()
            row["Charging End Time"]   = datetime.fromisoformat(row["Charging End Time"]).isoformat()
            writer.writerow({k: row.get(k, "") for k in fieldnames})

def transform_nrel_stations(raw_json, output_csv):
    """Extract station fields from NREL JSON for staging."""
    with open(raw_json) as f, open(output_csv, 'w', newline='') as outfile:
        data = json.load(f)["fuel_stations"]
        fieldnames = [
            "station_id", "station_name", "street_address", "city", "state",
            "zip", "country", "latitude", "longitude", "ev_connector_types",
            "access_days_time", "station_type"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for rec in data:
            connectors = rec.get("ev_connector_types")
            connector_str = "|".join(connectors) if isinstance(connectors, list) else ""
            writer.writerow({
                "station_id": rec.get("id"),
                "station_name": rec.get("station_name"),
                "street_address": rec.get("street_address"),
                "city": rec.get("city"),
                "state": rec.get("state"),
                "zip": rec.get("zip"),
                "country": rec.get("country"),
                "latitude": rec.get("latitude"),
                "longitude": rec.get("longitude"),
                "ev_connector_types": connector_str,
                "access_days_time": rec.get("access_days_time"),
                "station_type": rec.get("station_type")
            })

def transform_weather(raw_json, output_csv):
    """Extract weather fields from OpenWeatherMap JSON for staging."""
    with open(raw_json) as f, open(output_csv, 'w', newline='') as outfile:
        records = json.load(f)["weather_data"]
        fieldnames = [
            "extraction_timestamp", "city", "weather_main",
            "weather_description", "temp_celsius", "humidity", "wind_speed"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for rec in records:
            # Default values
            weather_main = ""
            weather_desc = ""
            # Iterate through weather entries list
            for weather_item in rec.get("weather", []):
                if isinstance(weather_item, dict):
                    weather_main = weather_item.get("main", "")
                    weather_desc = weather_item.get("description", "")
                    break  # Only need first entry

            main = rec.get("main") or {}
            wind = rec.get("wind") or {}

            writer.writerow({
                "extraction_timestamp": rec.get("extraction_timestamp", ""),
                "city": rec.get("name", ""),
                "weather_main": weather_main,
                "weather_description": weather_desc,
                "temp_celsius": main.get("temp", ""),
                "humidity": main.get("humidity", ""),
                "wind_speed": wind.get("speed", "")
            })

if __name__ == "__main__":
    # EV sessions
    raw_csv = RAW_DIR / "ev_charging_patterns.csv"
    out_csv = PROCESSED_DIR / "ev_sessions_transformed.csv"
    transform_ev_sessions(raw_csv, out_csv)
    print(f"EV sessions transformed to {out_csv}")

    # NREL stations
    raw_nrel = sorted(RAW_DIR.glob("nrel_stations_*.json"))[-1]
    out_nrel = PROCESSED_DIR / "nrel_stations_transformed.csv"
    transform_nrel_stations(raw_nrel, out_nrel)
    print(f"NREL stations transformed to {out_nrel}")

    # Weather data
    raw_weather = sorted(RAW_DIR.glob("weather_data_*.json"))[-1]
    out_weather = PROCESSED_DIR / "weather_transformed.csv"
    transform_weather(raw_weather, out_weather)
    print(f"Weather data transformed to {out_weather}")
