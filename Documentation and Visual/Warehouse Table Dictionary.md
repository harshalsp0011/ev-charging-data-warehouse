# EV Charging Data Warehouse — Data Dictionary

Generated: 2025-08-12

## Fact Table: FACT_CHARGING_SESSIONS

| Column                    | Type       | Nullable | Description                                                                  | Notes                                                                         |
|---------------------------|------------|----------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| session_id                | STRING     | NO       | Unique identifier for each charging session                                  | Generated from hash(User ID + Start Timestamp)                                |
| user_id                   | INTEGER    | NO       | Identifier for the user who charged                                          | From `User ID`                                                                |
| station_id                | STRING     | NO       | Identifier for the charging station                                          | From `Charging Station ID`                                                     |
| date_id                   | INTEGER    | NO       | Surrogate key linking to DIM_TIME                                             | Derived from `Charging Start Time`                                            |
| start_timestamp           | TIMESTAMP  | NO       | Timestamp when charging started                                              | From `Charging Start Time`                                                    |
| end_timestamp             | TIMESTAMP  | NO       | Timestamp when charging ended                                                | From `Charging End Time`                                                      |
| energy_consumed_kwh       | FLOAT      | YES      | Total energy consumed (kWh)                                                   | 66 missing values—impute via rate * duration or flag                          |
| duration_hours            | FLOAT      | NO       | Total charging duration in hours                                              | From `Charging Duration (hours)`                                              |
| charging_rate_kw          | FLOAT      | YES      | Average charging power (kW)                                                    | 66 missing values—same handling as energy_consumed_kwh                         |
| charging_cost_usd         | FLOAT      | NO       | Total cost of the charging session (USD)                                       |                                                                              |
| distance_driven_km        | FLOAT      | YES      | Distance driven since last charge (km)                                         | 66 missing values—impute or flag                                              |
| start_soc_percent         | INTEGER    | NO       | Battery state of charge at start (%)                                           | Values >100% capped at 100                                                  |
| end_soc_percent           | INTEGER    | NO       | Battery state of charge at end (%)                                             | Values >100% capped at 100                                                  |

## Dimension Tables

### DIM_USER

| Column    | Type    | Nullable | Description                                    |
|-----------|---------|----------|------------------------------------------------|
| user_id   | INTEGER | NO       | Unique user identifier                         |
| user_type | STRING  | NO       | User classification (Commuter, Traveler, etc.) |

### DIM_STATION

| Column               | Type   | Nullable | Description                                 |
|----------------------|--------|----------|---------------------------------------------|
| station_id           | STRING | NO       | Unique station identifier                   |
| station_location     | STRING | NO       | City where the station is located           |
| charger_type         | STRING | NO       | Charger type (Level 1, Level 2, DC Fast)    |

### DIM_VEHICLE

| Column                  | Type    | Nullable | Description                                     |
|-------------------------|---------|----------|-------------------------------------------------|
| vehicle_model           | STRING  | NO       | EV model name                                   |
| battery_capacity_kwh    | FLOAT   | NO       | Battery capacity (kWh)                          |
| vehicle_age_years       | FLOAT   | NO       | Vehicle age in years                            |

### DIM_TIME

| Column            | Type      | Nullable | Description                                          |
|-------------------|-----------|----------|------------------------------------------------------|
| date_id           | INTEGER   | NO       | Surrogate date key derived from timestamp            |
| date              | DATE      | NO       | Date part of the charging start time                 |
| day_of_week       | STRING    | NO       | Day name (Monday–Sunday)                             |
| time_of_day       | STRING    | NO       | Segment (Morning, Afternoon, Evening, Night)         |
| hour              | INTEGER   | NO       | Hour of day (0–23)                                   |

### DIM_WEATHER

| Column           | Type    | Nullable | Description                                   |
|------------------|---------|----------|-----------------------------------------------|
| date_id          | INTEGER | NO       | Surrogate date key (same as DIM_TIME)         |
| temperature_c    | FLOAT   | NO       | Ambient temperature in Celsius                |



## Data Quality & Cleaning Summary

- **Energy Consumed (kWh)**: 5.0% missing — impute via `charging_rate_kw * duration_hours` or flag  
- **Charging Rate (kW)**: 5.0% missing — same imputation  
- **Distance Driven (km)**: 5.0% missing — impute or flag  
- **State of Charge**: Values >100% — cap at 100%  
- **Outliers**: Small number of outliers in numeric fields to review case-by-case  
