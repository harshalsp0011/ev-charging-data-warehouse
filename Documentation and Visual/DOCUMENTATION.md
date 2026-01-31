# EV Charging Data Warehouse - Complete Documentation

**Last Updated:** January 30, 2026  
**Project Type:** Cloud Data Warehouse (Star Schema Design)  
**Tech Stack:** Python, Snowflake, SQL, Jupyter, Pandas, Streamlit

---

## 📌 Quick Navigation
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Star Schema Design](#star-schema-design)
- [Data Dictionary](#data-dictionary)
- [Setup & Installation](#setup--installation)
- [Usage Guide](#usage-guide)
- [Data Flow](#data-flow)
- [File Locations](#file-locations)

---

## 🎯 Project Overview

### **What is This?**
A cloud-based data warehouse using **Snowflake** for EV charging station analytics, focusing on optimization and demand forecasting in the electric vehicle ecosystem.

### **Key Objectives**
- Analyze EV charging patterns and station utilization
- Predict charging demand based on temporal and weather factors
- Optimize charging network infrastructure
- Provide interactive dashboards for stakeholders

### **Key Features**
- ✅ Real-time data processing with automated ETL pipelines
- ✅ Star schema design optimized for analytics
- ✅ Predictive analytics for demand forecasting
- ✅ Interactive dashboards with Streamlit
- ✅ Weather correlation analysis
- ✅ Cost-optimized using free/student tiers

### **Project Scope**
- **Domain:** Electric Vehicles / Smart Mobility
- **Duration:** 18-24 weeks
- **Resources:** Free tiers and student accounts only

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Data Warehouse** | Snowflake (Student Trial) | Cloud-based data storage and processing |
| **ETL Pipeline** | Python, Apache Airflow | Data extraction, transformation, loading |
| **Analytics** | Python (Pandas, NumPy) | Statistical analysis and calculations |
| **Visualization** | Streamlit, Plotly | Interactive dashboards and charts |
| **Data Sources** | Kaggle CSV, NREL API, OpenWeatherMap | Raw session, station, and weather data |
| **Development** | VS Code, Jupyter Notebooks | Code development and exploration |
| **Version Control** | Git, GitHub | Source code management |
| **Environment** | Python Virtual Environment (ev_env) | Package isolation |

### **Python Dependencies**
```
pandas>=1.5.0
numpy>=1.23.0
sqlalchemy>=1.4.0
snowflake-connector-python>=3.0.0
snowflake-sqlalchemy>=1.4.0
apache-airflow>=2.5.0
streamlit>=1.20.0
plotly>=5.10.0
requests>=2.28.0
python-dotenv>=0.19.0
great-expectations>=0.15.0
pytest>=7.0.0
jupyter>=1.0.0
```

---

## 📁 Project Structure

```
ev-charging-data-warehouse/
│
├── 📄 DOCUMENTATION.md                   # This file - complete guide
├── 📄 README.md                          # Quick start guide
├── 📄 LICENSE                            # Project license
├── 📄 requirements.txt                   # Python dependencies
├── 📄 .env                               # Environment variables (git-ignored)
├── 📄 .env.example                       # Environment template
│
├── 🐍 ROOT SCRIPTS
│   ├── analyze_kaggle_data.py            # Data analysis script
│   ├── preview_kaggle_data.py            # Data preview script
│   ├── test_environment.py               # Environment verification
│   └── data_preview and analysis.ipynb   # Main analysis notebook
│
├── 📊 data/
│   ├── external/                         # Third-party raw datasets
│   │   └── ev_charging_patterns.csv     # Kaggle dataset (1,320 records)
│   ├── raw/                              # Downloaded from APIs
│   │   ├── ev_charging_patterns.csv
│   │   ├── nrel_stations_*.json          # NREL stations data
│   │   └── weather_data_*.json           # Weather API data
│   └── processed/                        # Cleaned data ready for warehouse
│
├── 🗄️ sql/
│   ├── ddl/                              # Data Definition Language
│   │   ├── create_dims.sql               # Dimension tables DDL
│   │   └── create_fact_charging.sql      # Fact table DDL
│   ├── dml/                              # Data Manipulation (future)
│   └── analytics/                        # Analytical queries (future)
│
├── 💻 src/
│   ├── data_sources/                     # API integrations
│   │   ├── nrel_api.py                   # NREL API connector
│   │   └── weather_api.py                # Weather API connector
│   ├── etl/                              # ETL pipeline
│   │   ├── transform.py                  # Data transformation
│   │   ├── load.py                       # Snowflake loader
│   │   └── data_quality.py               # Data validation
│   ├── database/
│   │   └── snowflake_connector.py        # DB connection utility
│   ├── analytics/                        # KPI calculations (future)
│   └── visualization/                    # Dashboards (future)
│
├── 📖 docs/
│   ├── data_dictionary.md                # Column definitions
│   └── schema_ddl.sql                    # Schema reference
│
├── 🧪 tests/
│   ├── test_nrel_api.py                  # API tests
│   ├── test_weather_api.py               # API tests
│   ├── sample_nrel_stations.csv          # Test data
│   └── sample_weather_data.csv           # Test data
│
├── 📋 reports/                           # Analysis outputs
│   ├── data_quality_report.txt           # Data quality findings
│   ├── numeric_summary.csv               # Statistics
│   ├── sample_data.csv                   # Data samples
│   ├── CSV to Table structure.png        # Mapping diagram
│   ├── Data Flow Mapping.png             # Flow visualization
│   ├── ER Diagram.png                    # Schema diagram
│   └── end-to-end project workflow.png   # Workflow diagram
│
├── 📝 config/
│   └── api_config.py                     # API configuration
│
└── 🔧 ev_env/                            # Virtual environment
    └── (bin/, lib/, share/)
```

---

## 📡 Data Sources

### **1. Kaggle EV Charging Patterns (CSV)**
- **File:** `data/external/ev_charging_patterns.csv`
- **Records:** 1,320 charging sessions
- **Columns:** 20 fields including user info, vehicle specs, charging metrics
- **Source:** Synthetic dataset from Kaggle
- **Status:** ✅ Loaded and analyzed

### **2. NREL Alternative Fuel Station Locator API**
- **Purpose:** EV charging station metadata (location, type, operator)
- **API:** U.S. Department of Energy - National Renewable Energy Lab
- **Output:** `data/raw/nrel_stations_*.json`
- **Key Fields:** Station ID, coordinates, charger types, access
- **Status:** ✅ API integration complete

### **3. OpenWeatherMap API**
- **Purpose:** Weather conditions (temperature, humidity, conditions)
- **Output:** `data/raw/weather_data_*.json`
- **Key Fields:** Temperature, humidity, weather description
- **Status:** ✅ API integration complete

---

## 🌟 Star Schema Design

### **Architecture Overview**
```
                    ┌─────────────────┐
                    │  FACT_CHARGING  │
                    │    SESSIONS     │
                    │  (1,320 rows)   │
                    └────────┬────────┘
           ┌────────────┬────┴─────┬───────────┬──────────┐
           ▼            ▼          ▼           ▼          ▼
      ┌─────────┐  ┌──────────┐ ┌────────┐ ┌──────────┐ ┌──────────┐
      │DIM_USER │  │DIM_TIME  │ │DIM_    │ │DIM_      │ │DIM_      │
      │         │  │          │ │STATION │ │VEHICLE   │ │WEATHER   │
      │50 users │  │365+ days │ │50      │ │20 models │ │~365 days │
      └─────────┘  └──────────┘ │stations│ └──────────┘ └──────────┘
                                 └────────┘
```

### **Fact Table: FACT_CHARGING_SESSIONS**
**Purpose:** Store transactional charging session data

**Measures (Metrics):**
- `energy_consumed_kwh` - Total energy consumed
- `charging_cost_usd` - Session cost
- `duration_hours` - Charging duration
- `charging_rate_kw` - Average charging power
- `start_soc_percent` - Battery level at start (0-100)
- `end_soc_percent` - Battery level at end (0-100)
- `distance_driven_km` - Distance since last charge

**Dimensions (Foreign Keys):**
- `user_id` → DIM_USER
- `station_id` → DIM_STATION
- `vehicle_id` → DIM_VEHICLE
- `date_id` → DIM_TIME
- `weather_id` → DIM_WEATHER

### **Dimension Tables**

#### **DIM_USER** (~50 rows)
- `user_id` (PK) - Unique user identifier
- `user_type` - Category (Commuter, Casual, Traveler, etc.)

#### **DIM_VEHICLE** (~20 rows)
- `vehicle_id` (PK) - Vehicle model identifier
- `vehicle_model` - Model name
- `battery_capacity_kwh` - Battery capacity
- `vehicle_age_years` - Age in years

#### **DIM_STATION** (~50 rows)
- `station_id` (PK) - Station identifier
- `station_location` - City/address
- `charger_type` - Level 1, Level 2, or DC Fast Charger
- `network_operator` - Station operator name

#### **DIM_TIME** (365+ rows)
- `date_id` (PK) - Surrogate key
- `date_value` - Actual date
- `year`, `month`, `day` - Date components
- `day_of_week` - Monday-Sunday
- `hour` - Hour of day (0-23)
- `time_of_day` - Morning/Afternoon/Evening/Night
- `is_weekend` - Boolean flag

#### **DIM_WEATHER** (~365 rows)
- `weather_id` (PK) - Surrogate key
- `date_value` - Date
- `temperature_celsius` - Temperature
- `humidity_percent` - Humidity
- `weather_condition` - Clear/Cloudy/Rain/Snow

---

## 📖 Data Dictionary

### **FACT_CHARGING_SESSIONS**

| Column | Type | Nullable | Description | Source | Notes |
|--------|------|----------|-------------|--------|-------|
| session_id | STRING | NO | Unique session ID | Generated | Hash(User ID + Start Time) |
| user_id | INTEGER | NO | User identifier | CSV: User ID | FK to DIM_USER |
| station_id | STRING | NO | Station identifier | CSV: Charging Station ID | FK to DIM_STATION |
| vehicle_id | STRING | NO | Vehicle identifier | CSV: Vehicle Model | FK to DIM_VEHICLE |
| date_id | INTEGER | NO | Date identifier | Derived from start_timestamp | FK to DIM_TIME |
| weather_id | INTEGER | NO | Weather identifier | Derived from date | FK to DIM_WEATHER |
| start_timestamp | TIMESTAMP_LTZ | NO | Session start | CSV: Charging Start Time | Timezone aware |
| end_timestamp | TIMESTAMP_LTZ | NO | Session end | CSV: Charging End Time | Timezone aware |
| energy_consumed_kwh | FLOAT | YES | Energy consumed | CSV: Energy Consumed (kWh) | 66 missing values |
| duration_hours | FLOAT | NO | Charging duration | CSV: Charging Duration (hours) | |
| charging_rate_kw | FLOAT | YES | Charging power | CSV: Charging Rate (kW) | 66 missing values |
| charging_cost_usd | FLOAT | NO | Session cost | CSV: Charging Cost (USD) | |
| distance_driven_km | FLOAT | YES | Distance driven | CSV: Distance Driven... | 66 missing values |
| start_soc_percent | INTEGER | NO | Start battery % | CSV: State of Charge (Start %) | Cap at 100 |
| end_soc_percent | INTEGER | NO | End battery % | CSV: State of Charge (End %) | Cap at 100 |

### **DIM_USER**
| Column | Type | Nullable | Description | Source |
|--------|------|----------|-------------|--------|
| user_id | INTEGER | NO | Unique user ID | CSV: User ID |
| user_type | STRING | NO | User category | CSV: User Type |

### **DIM_VEHICLE**
| Column | Type | Nullable | Description | Source |
|--------|------|----------|-------------|--------|
| vehicle_id | STRING | NO | Vehicle model ID | CSV: Vehicle Model |
| vehicle_model | STRING | NO | Model name | CSV: Vehicle Model |
| battery_capacity_kwh | FLOAT | NO | Battery capacity | CSV: Battery Capacity (kWh) |
| vehicle_age_years | FLOAT | NO | Vehicle age | CSV: Vehicle Age (years) |

### **DIM_STATION**
| Column | Type | Nullable | Description | Source |
|--------|------|----------|-------------|--------|
| station_id | STRING | NO | Station ID | CSV: Charging Station ID |
| station_location | STRING | NO | Location | CSV: Charging Station Location |
| charger_type | STRING | NO | Charger type | CSV: Charger Type |
| network_operator | STRING | YES | Operator name | NREL API (future) |

### **DIM_TIME**
| Column | Type | Nullable | Description | Source |
|--------|------|----------|-------------|--------|
| date_id | INTEGER | NO | Surrogate key | Generated |
| date_value | DATE | NO | Actual date | Derived |
| year | INTEGER | NO | Year | Extracted |
| month | INTEGER | NO | Month (1-12) | Extracted |
| day | INTEGER | NO | Day (1-31) | Extracted |
| day_of_week | STRING | NO | Mon-Sun | CSV: Day of Week |
| hour | INTEGER | NO | Hour (0-23) | Extracted |
| time_of_day | STRING | NO | Morning/Evening | CSV: Time of Day |
| is_weekend | BOOLEAN | NO | Weekend flag | Calculated |

### **DIM_WEATHER**
| Column | Type | Nullable | Description | Source |
|--------|------|----------|-------------|--------|
| weather_id | INTEGER | NO | Surrogate key | Generated |
| date_value | DATE | NO | Date | Matched |
| temperature_celsius | FLOAT | NO | Temperature | CSV: Temperature (°C) |
| humidity_percent | FLOAT | YES | Humidity | Weather API (future) |
| weather_condition | STRING | YES | Condition | Weather API (future) |

---

## 🚀 Setup & Installation

### **Prerequisites**
- Python 3.8+
- Snowflake account (student trial)
- API keys (NREL, OpenWeatherMap)
- Git

### **1. Clone Repository**
```bash
git clone <repository-url>
cd ev-charging-data-warehouse
```

### **2. Create Virtual Environment**
```bash
python3 -m venv ev_env
source ev_env/bin/activate  # macOS/Linux
# or
ev_env\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create `.env` file from template:
```bash
cp .env.example .env
```

Edit `.env`:
```
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=EV_CHARGING_DW
SNOWFLAKE_SCHEMA=ANALYTICS

NREL_API_KEY=your_nrel_key
WEATHER_API_KEY=your_openweathermap_key
```

### **5. Test Environment**
```bash
python test_environment.py
```

### **6. Run Analysis Notebook**
```bash
jupyter notebook "data_preview and analysis.ipynb"
```

---

## 📚 Usage Guide

### **Running Data Analysis**
```bash
# Open Jupyter notebook
jupyter notebook "data_preview and analysis.ipynb"

# Or run Python script
python analyze_kaggle_data.py
```

### **Fetching API Data**
```python
# Fetch NREL stations
python -c "from src.data_sources.nrel_api import fetch_stations; fetch_stations()"

# Fetch weather data
python -c "from src.data_sources.weather_api import fetch_weather; fetch_weather()"
```

### **Running ETL Pipeline**
```python
from src.etl.transform import transform_ev_sessions
from src.etl.load import load_dimensions, load_fact_table

# Transform data
transform_ev_sessions('data/raw/ev_charging_patterns.csv', 'data/processed/sessions.csv')

# Load to Snowflake
load_dimensions()
load_fact_table()
```

### **Testing**
```bash
# Test API connections
pytest tests/test_nrel_api.py
pytest tests/test_weather_api.py

# Run all tests
pytest tests/
```

---

## 🔄 Data Flow

### **End-to-End Pipeline**

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA SOURCES                              │
├─────────────┬──────────────────────────┬────────────────────┤
│ Kaggle CSV  │ NREL API                 │ OpenWeatherMap API │
└──────┬──────┴──────────────────┬───────┴────────────────────┘
       │                         │
       ▼                         ▼
   [data/external/]         [data/raw/]
       │                         │
       └──────────┬──────────────┘
                  ▼
    ┌─────────────────────────┐
    │  DATA ANALYSIS          │  ← Jupyter Notebook
    │  - Quality checks       │    (data_preview and analysis.ipynb)
    │  - Schema design        │
    │  - Cleaning needs       │
    └──────────┬──────────────┘
               ▼
    ┌─────────────────────────┐
    │  TRANSFORMATION         │  ← src/etl/transform.py
    │  - Parse timestamps     │
    │  - Normalize formats    │
    │  - Handle missing data  │
    └──────────┬──────────────┘
               ▼
         [data/processed/]
               ▼
    ┌─────────────────────────┐
    │  DATA QUALITY           │  ← src/etl/data_quality.py
    │  - Validate types       │
    │  - Check nulls          │
    │  - Verify integrity     │
    └──────────┬──────────────┘
               ▼
    ┌─────────────────────────────────────┐
    │  SNOWFLAKE DATA WAREHOUSE           │
    ├─────────────────────────────────────┤
    │  sql/ddl/create_dims.sql            │
    │  - DIM_USER                         │
    │  - DIM_VEHICLE                      │
    │  - DIM_STATION                      │
    │  - DIM_TIME                         │
    │  - DIM_WEATHER                      │
    │                                     │
    │  sql/ddl/create_fact_charging.sql   │
    │  - FACT_CHARGING_SESSIONS           │
    └──────────┬──────────────────────────┘
               ▼
    ┌─────────────────────────┐
    │  ANALYTICS & REPORTING  │  ← src/analytics/ (future)
    │  - KPI calculations     │
    │  - Demand forecasting   │
    │  - Utilization metrics  │
    └──────────┬──────────────┘
               ▼
    ┌─────────────────────────┐
    │  VISUALIZATION          │  ← src/visualization/ (future)
    │  - Streamlit dashboard  │
    │  - Plotly charts        │
    │  - Reports              │
    └─────────────────────────┘
```

---

## 📍 File Locations Reference

### **Configuration**
- Environment variables: `.env`
- API config: `config/api_config.py`
- Requirements: `requirements.txt`

### **Data Files**
- Original dataset: `data/external/ev_charging_patterns.csv`
- API data: `data/raw/*.json`
- Processed data: `data/processed/` (output)

### **Analysis & Reports**
- Main notebook: `data_preview and analysis.ipynb`
- Quality report: `reports/data_quality_report.txt`
- Visual diagrams: `reports/*.png`

### **SQL Scripts**
- Dimension tables: `sql/ddl/create_dims.sql`
- Fact table: `sql/ddl/create_fact_charging.sql`

### **Python Source Code**
- API connectors: `src/data_sources/*.py`
- ETL pipeline: `src/etl/*.py`
- DB utilities: `src/database/snowflake_connector.py`

### **Testing**
- API tests: `tests/test_*_api.py`
- Test data: `tests/sample_*.csv`

---

## 🎯 Project Status

### ✅ **Completed**
- Data extraction from APIs
- Comprehensive data analysis
- Star schema design (DDL)
- Data quality assessment
- Visual documentation
- ETL transformation logic
- Database connector

### 🚧 **In Progress**
- Data loading to Snowflake
- ETL pipeline automation

### 📋 **Planned**
- SQL DML scripts (INSERT/UPDATE)
- Analytical queries
- Dashboard/visualization
- Airflow DAG orchestration

---

## 📞 Key Contacts & Resources

### **APIs**
- **NREL API Docs:** https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/
- **OpenWeatherMap API:** https://openweathermap.org/api

### **Documentation**
- **Snowflake Docs:** https://docs.snowflake.com/
- **Pandas Docs:** https://pandas.pydata.org/docs/
- **Streamlit Docs:** https://docs.streamlit.io/

---

## 📝 Notes

### **Data Quality Issues Identified**
- 66 missing values in energy_consumed_kwh
- 66 missing values in charging_rate_kw
- 66 missing values in distance_driven_km
- Some State of Charge values >100% (need capping)

### **Recommended Next Steps**
1. Implement missing value imputation strategy
2. Cap State of Charge values at 100%
3. Create staging tables in Snowflake
4. Develop Airflow DAG for automation
5. Build Streamlit dashboard prototype

---

**End of Documentation**
