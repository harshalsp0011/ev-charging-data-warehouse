# EV Charging Data Warehouse Project - Complete Reference Guide

## Project Overview
**Project Name:** EV Charging Network Data Warehouse  
**Objective:** Build an end-to-end data warehouse for analyzing electric vehicle charging patterns, station utilization, and weather correlations using real-time APIs and synthetic data.

---

## Architecture & Technology Stack

### **Data Sources**
- **NREL Alternative Fuel Station Locator API** - EV charging station metadata
- **OpenWeatherMap API** - Weather conditions data
- **Synthetic EV Charging Sessions CSV** - Charging transaction data (1,320 records)

### **Technology Stack**
| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Cloud Data Warehouse** | Snowflake | Latest | Data storage, processing, analytics |
| **Programming Language** | Python | 3.x | ETL scripts, data transformation |
| **Environment Management** | Virtual Environment (ev_env) | - | Package isolation |
| **Database Connector** | snowflake-connector-python | Latest | Python-Snowflake integration |
| **Data Processing** | pandas | 2.1.4 | Data manipulation and analysis |
| **API Requests** | requests library | Latest | HTTP API calls |
| **Environment Variables** | python-dotenv | Latest | Configuration management |
| **Orchestration** | Apache Airflow | Future | ETL pipeline scheduling |
| **Visualization** | Streamlit + Plotly | 1.46.1 + 6.2.0 | Dashboard and reporting |

---

## Project Structure

```
ev-charging-data-warehouse/
├── config/
│   ├── api_config.py              # API keys, endpoints, settings
│   └── snowflake_config.py        # Database connection parameters
├── src/
│   ├── data_sources/
│   │   ├── nrel_api.py            # NREL API extraction script
│   │   └── weather_api.py         # OpenWeatherMap API extraction
│   ├── etl/
│   │   ├── extract.py             # Data extraction logic
│   │   ├── transform.py           # Data transformation and cleaning
│   │   ├── load.py                # Snowflake loading operations
│   │   └── data_quality.py        # Data validation functions
│   ├── database/
│   │   └── snowflake_connector.py # Database connection utilities
│   ├── analytics/
│   │   └── [Future KPI calculations, forecasting models]
│   └── visualization/
│       └── [Future Streamlit dashboards]
├── sql/
│   ├── ddl/
│   │   ├── create_schemas.sql     # Database schema creation
│   │   ├── create_dimensions.sql  # Dimension table DDL
│   │   └── create_fact_tables.sql # Fact table DDL
│   ├── dml/
│   │   └── [Data manipulation scripts]
│   └── analytics/
│       └── [Analytical queries and reports]
├── data/
│   ├── raw/                       # Unprocessed API responses, original CSVs
│   │   ├── ev_charging_patterns.csv
│   │   ├── nrel_stations_YYYYMMDD_HHMMSS.json
│   │   ├── weather_data_YYYYMMDD_HHMMSS.json
│   │   └── sample_nrel_data.json
│   ├── processed/                 # Cleaned, transformed data
│   │   ├── ev_sessions_transformed.csv
│   │   ├── nrel_stations_transformed.csv
│   │   └── weather_transformed.csv
│   └── external/                  # Reference data, lookup tables
├── tests/
│   └── [Unit tests and integration tests]
├── docs/
│   └── [Project documentation]
├── notebooks/
│   └── [Jupyter notebooks for exploration]
├── logs/
│   └── [Application logs and monitoring]
├── .env                           # Environment variables (API keys, credentials)
└── requirements.txt               # Python dependencies
```

---

## Snowflake Database Architecture

### **Database:** `EV_CHARGING_DW`

#### **Schemas:**
| Schema Name | Purpose | Contents |
|-------------|---------|----------|
| **RAW_DATA** | Data ingestion | Internal stage (`EXT_STAGE`) for file uploads |
| **STAGING** | Data transformation | Intermediate tables for ETL processing |
| **ANALYTICS** | Production analytics | Star schema (dimensions + fact table) |
| **SANDBOX** | Development/testing | Experimental tables and queries |

#### **Warehouses:**
| Warehouse Name | Size | Purpose |
|----------------|------|---------|
| **EV_DEV_WH** | X-Small | Development, ETL operations |
| **EV_ANALYTICS_WH** | Small | Production analytics, dashboards |

---

## Star Schema Design

### **Dimension Tables:**
| Table | Rows | Description | Key Fields |
|-------|------|-------------|------------|
| **DIM_USER** | 1,320 | User profiles and types | user_id, user_type, audit_timestamp |
| **DIM_VEHICLE** | 5 | Vehicle models and specs | vehicle_id, vehicle_model, battery_capacity_kwh, vehicle_age_years |
| **DIM_STATION** | 462 | Charging station details | station_id, station_location, charger_type, audit_timestamp |
| **DIM_TIME** | 1,320 | Time dimension | date_id, date_value, year, month, day, weekday, time_of_day, hour |
| **DIM_WEATHER** | 1,320 | Weather conditions | weather_id, date_id, location, temperature_celsius, weather_main, humidity_percent |

### **Fact Table:**
| Table | Rows | Description | Key Measures |
|-------|------|-------------|--------------|
| **FACT_CHARGING_SESSIONS** | 1,320 | Charging session transactions | energy_consumed_kwh, duration_hours, charging_rate_kw, charging_cost_usd, distance_driven_km, start_soc_percent, end_soc_percent |

### **Staging Tables:**
| Table | Purpose | Source |
|-------|---------|--------|
| **stg_ev_sessions** | EV session staging | ev_charging_patterns.csv |
| **stg_nrel_stations** | Station metadata staging | NREL API JSON |
| **stg_weather** | Weather data staging | OpenWeatherMap API JSON |

---

## API Configuration

### **NREL Alternative Fuel Station Locator API**
- **Base URL:** `https://developer.nrel.gov/api/alt-fuel-stations/v1`
- **Authentication:** API Key required
- **Rate Limits:** Standard government API limits
- **Data Extracted:** Station locations, charger types, access information

### **OpenWeatherMap API**
- **Base URL:** `https://api.openweathermap.org/data/2.5`
- **Authentication:** API Key required  
- **Rate Limits:** 1000 calls/day (free tier)
- **Data Extracted:** Current weather, temperature, humidity, wind speed

### **Environment Variables (.env file):**
```bash
# API Keys
NREL_API_KEY=your_nrel_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here

# Snowflake Configuration
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=EV_DEV_WH
SNOWFLAKE_DATABASE=EV_CHARGING_DW
SNOWFLAKE_SCHEMA=RAW_DATA
```

---

## Completed Tasks Summary

### **Task 1: Project Initialization**
- ✅ Project folder structure created
- ✅ Requirements and objectives defined

### **Task 2: Python Environment Setup** 
- ✅ Virtual environment (ev_env) created and activated
- ✅ Core packages installed: pandas, snowflake-connector-python, streamlit, plotly, numpy, sqlalchemy, jupyter, pytest

### **Task 3: Register Free Accounts**
- ✅ Snowflake account activated
- ✅ NREL API key obtained  
- ✅ OpenWeatherMap API key obtained

### **Task 4: Explore & Download Sample Data**
- ✅ Sample EV charging patterns CSV (1,320 records)
- ✅ NREL station data JSON samples
- ✅ Weather data JSON samples

### **Task 5: Implement Star Schema in Snowflake**
- ✅ **5.1:** Created database (`EV_CHARGING_DW`) and schemas (RAW_DATA, STAGING, ANALYTICS, SANDBOX)
- ✅ **5.2:** Created warehouses (EV_DEV_WH, EV_ANALYTICS_WH)
- ✅ **5.3:** Executed DDL for all dimension and fact tables
- ✅ **5.4:** Loaded sample data into staging and analytics tables
- ✅ **5.5:** Validated data load with row counts and referential integrity checks

### **Task 6: Build ETL Pipelines** (In Progress)
- ✅ **6.1:** Developed extraction scripts for NREL & Weather APIs
  - Created `src/data_sources/nrel_api.py` (extracted 500 stations)
  - Created `src/data_sources/weather_api.py` (extracted 10 cities)
- ✅ **6.2:** Transformed raw CSV & API data to match star schema
  - Created `src/etl/transform.py` for data normalization
  - Generated processed CSVs with validation (1,320 sessions, 500 stations, 10 weather records)
- 🔄 **6.3:** Load transformed data into Snowflake (Currently debugging staging table loading)
- ⏳ **6.4:** Orchestrate with Apache Airflow
- ⏳ **6.5:** Implement data quality checks & alerts

---

## Current Issue Status

### **Problem:** 
In Task 6.3, while loading transformed CSVs into Snowflake staging tables:
- `stg_ev_sessions` loads successfully (1,320 rows)
- `stg_nrel_stations` and `stg_weather` remain at 0 rows despite successful PUT commands

### **Investigation Steps Taken:**
1. Verified file transformation created correct CSVs in `data/processed/`
2. Confirmed staging table schema compatibility
3. Attempted stage name corrections (`@RAW_DATA.EXT_STAGE` vs `@RAW_DATA.ext_stage`)
4. Ready to debug with `LIST @EXT_STAGE` and manual COPY commands

---

## Upcoming Tasks Roadmap

### **Task 7: Generate Synthetic Data**
- Scale up dataset with additional synthetic charging sessions
- Generate diverse user patterns and seasonal variations

### **Task 8: Snowflake Database Optimization**  
- Implement clustering keys and search optimization
- Create materialized views for common queries
- Optimize warehouse sizing and auto-suspend settings

### **Task 9: Analytics Script Development**
- Build KPI calculation functions
- Develop demand forecasting models
- Create utilization analysis algorithms

### **Task 10: Dashboard Creation & Deployment**
- Design Streamlit dashboard interface
- Implement interactive Plotly visualizations
- Deploy dashboard with real-time data connections

### **Task 11: Monitoring, Refinement & Reporting**
- Set up Great Expectations data quality framework
- Implement Airflow monitoring and alerting
- Create automated reporting and notifications

---

## Key Data Validation Results

### **Schema Validation (Task 5.5):**
```
Row Counts:
- DIM_USER: 1,320
- DIM_VEHICLE: 5  
- DIM_STATION: 462
- DIM_TIME: 1,320
- DIM_WEATHER: 1,320
- FACT_CHARGING_SESSIONS: 1,320

Referential Integrity: All FK relationships verified (0 missing keys)
Dimension Coverage: 100% coverage across all dimensions
```

### **ETL Transformation Results (Task 6.2):**
```
data/processed/ev_sessions_transformed.csv: 1,320 records validated
data/processed/nrel_stations_transformed.csv: 500 records validated  
data/processed/weather_transformed.csv: 10 records validated
All expected columns present in each file
```

---

## Sample Queries and Use Cases

### **Business Intelligence Queries:**
```sql
-- Average energy consumption by vehicle model
SELECT v.vehicle_model, AVG(f.energy_consumed_kwh) AS avg_kwh
FROM FACT_CHARGING_SESSIONS f
JOIN DIM_VEHICLE v ON f.vehicle_id = v.vehicle_id
GROUP BY v.vehicle_model;

-- Charging session distribution by time of day
SELECT t.time_of_day, COUNT(*) AS sessions
FROM FACT_CHARGING_SESSIONS f
JOIN DIM_TIME t ON f.date_id = t.date_id
GROUP BY t.time_of_day;

-- Weather impact on energy consumption
SELECT w.temperature_celsius, AVG(f.energy_consumed_kwh) AS avg_consumption
FROM FACT_CHARGING_SESSIONS f
JOIN DIM_WEATHER w ON f.date_id = w.date_id
GROUP BY w.temperature_celsius
ORDER BY w.temperature_celsius;
```

---

## File Access and Navigation

### **Key Configuration Files:**
- **API Configuration:** `config/api_config.py`
- **Database Connection:** `src/database/snowflake_connector.py` 
- **Environment Variables:** `.env` (root directory)

### **Data Processing Scripts:**
- **NREL Extraction:** `src/data_sources/nrel_api.py`
- **Weather Extraction:** `src/data_sources/weather_api.py`
- **Data Transformation:** `src/etl/transform.py`
- **Snowflake Loading:** `src/etl/load.py`

### **SQL Scripts:**
- **Schema Creation:** `sql/ddl/create_schemas.sql`
- **Table Creation:** `sql/ddl/create_dimensions.sql`, `sql/ddl/create_fact_tables.sql`

---

## How to Continue This Project

### **To Resume from Current Point:**
```bash
# 1. Activate environment
source ev_env/bin/activate  # On macOS/Linux
# ev_env\Scripts\activate   # On Windows

# 2. Navigate to project directory
cd ev-charging-data-warehouse

# 3. Check current ETL status
python src/etl/load.py

# 4. Debug staging tables in Snowflake
# Run: LIST @RAW_DATA.EXT_STAGE; in Snowsight
```

### **To Start New Tasks:**
1. **Complete Task 6.3 debugging** (staging table loading)
2. **Begin Task 6.4** (Airflow orchestration setup)
3. **Install Airflow:** `pip install apache-airflow`
4. **Create DAG files** in new `airflow/dags/` directory

### **To Reference Previous Work:**
- All validation results and row counts are documented above
- File structure and naming conventions are established
- API extraction patterns are proven and working
- Star schema is fully implemented and validated

This reference guide contains everything needed to continue development, debug current issues, or hand off the project to another developer.