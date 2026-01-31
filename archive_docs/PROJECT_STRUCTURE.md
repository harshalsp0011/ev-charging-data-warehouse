# EV Charging Data Warehouse - Project Structure Guide

## 📁 Complete Directory Layout

```
ev-charging-data-warehouse/
│
├── 📄 README.md                          # Main project documentation
├── 📄 info.md                            # Additional project information
├── 📄 project-summary-reference.md       # Project reference summary
├── 📄 PROJECT_STRUCTURE.md               # This file - complete project guide
├── 📄 LICENSE                            # Project license
├── 📄 requirements.txt                   # Python dependencies
├── 📄 .env                               # Environment variables (git-ignored)
├── 📄 .env.example                       # Environment variables template
├── 📄 .gitignore                         # Git ignore rules
├── 📄 .gitattributes                     # Git attributes
│
├── 🐍 PYTHON SCRIPTS (Root Level)
│   ├── analyze_kaggle_data.py            # Kaggle data analysis script
│   ├── preview_kaggle_data.py            # Data preview and exploration
│   └── test_environment.py               # Environment setup verification
│
├── 📓 NOTEBOOKS (Root Level)
│   └── data_preview and analysis.ipynb   # Main data analysis notebook
│       ├── Section 1: Load & Inspect Data
│       ├── Section 2: Data Quality Analysis
│       ├── Section 3: Key Fields Analysis
│       ├── Section 4: Numeric Fields Analysis
│       ├── Section 5: DateTime Fields Analysis
│       ├── Section 6: Star Schema Mapping
│       ├── Section 7: Data Cleaning Requirements
│       ├── Section 8: Schema Recommendations
│       └── Section 9: Save Analysis Results
│
├── 📊 DATA/ (Data Pipeline)
│   ├── external/                        # External/raw data from sources
│   │   └── ev_charging_patterns.csv     # Kaggle EV charging dataset (original)
│   ├── raw/                             # Downloaded raw data from APIs
│   │   ├── ev_charging_patterns.csv     # EV charging session data
│   │   ├── nrel_stations_20250824_121038.json     # NREL API stations data
│   │   └── weather_data_20250824_121103.json      # Weather API data
│   └── processed/                       # Cleaned/transformed data (empty - ready for ETL output)
│
├── 🗄️ SQL/ (Data Warehouse DDL/DML)
│   ├── ddl/                             # Data Definition Language - Create tables
│   │   ├── create_dims.sql              # Dimension tables (DIM_USER, DIM_VEHICLE, DIM_STATION, DIM_TIME, DIM_WEATHER)
│   │   └── create_fact_charging.sql     # Fact table (FACT_CHARGING_SESSIONS)
│   ├── dml/                             # Data Manipulation Language (empty - ready for INSERT/UPDATE statements)
│   └── analytics/                       # Analytical queries (empty - ready for SELECT/aggregation queries)
│
├── 💻 SRC/ (Python ETL & Processing)
│   ├── data_sources/                    # API integrations & data collection
│   │   ├── nrel_api.py                  # NREL API connector for EV stations
│   │   └── weather_api.py               # OpenWeatherMap API connector
│   ├── etl/                             # Extract, Transform, Load processes
│   │   ├── transform.py                 # Data transformation/normalization
│   │   ├── load.py                      # Load data to Snowflake
│   │   └── data_quality.py              # Data validation & quality checks
│   ├── database/                        # Database connection management
│   │   └── snowflake_connector.py       # Snowflake connection utility
│   ├── analytics/                       # KPI calculations (empty - ready for analysis functions)
│   └── visualization/                   # Dashboard & reporting (empty - ready for Streamlit/Plotly)
│
├── 📖 DOCS/ (Documentation)
│   ├── data_dictionary.md               # Data fields documentation
│   └── schema_ddl.sql                   # Schema reference
│
├── 🧪 TESTS/ (Testing & Samples)
│   ├── test_nrel_api.py                 # NREL API tests
│   ├── test_weather_api.py              # Weather API tests
│   ├── sample_nrel_stations.csv         # Sample NREL data for testing
│   └── sample_weather_data.csv          # Sample weather data for testing
│
├── 📋 REPORTS/ (Analysis Output)
│   ├── data_quality_report.txt          # Data quality findings & issues
│   ├── numeric_summary.csv              # Numeric statistics summary
│   ├── sample_data.csv                  # Sample data preview
│   ├── consolidated visual mapping of CSV, NREL API, and weather attributes to star schema.csv  # Schema mapping
│   ├── CSV to Table structure.png       # Visual diagram of CSV mapping
│   ├── Data Flow Mapping.png            # Data flow visualization
│   ├── ER Diagram.png                   # Entity-relationship diagram
│   └── end-to-end project workflow.png  # Complete workflow diagram
│
├── 📝 CONFIG/ (Configuration)
│   └── api_config.py                    # API keys & endpoints configuration
│
├── 🔧 ENVIRONMENT
│   └── ev_env/                          # Python virtual environment
│       ├── bin/                         # Executables (python, pip, jupyter, streamlit, etc.)
│       ├── lib/                         # Python libraries
│       ├── share/                       # Shared data
│       ├── include/                     # C headers
│       └── pyvenv.cfg                   # Virtual environment config
│
└── 📚 NOTEBOOKS/ (Additional notebooks - empty, for future exploration)
```

---

## 📋 Folder Descriptions

### **Root Level Files**
- **README.md** - Overview of the project, tech stack, and features
- **PROJECT_STRUCTURE.md** - This guide - complete project documentation
- **info.md** - Additional project information
- **project-summary-reference.md** - Quick reference summary
- **requirements.txt** - All Python package dependencies
- **test_environment.py** - Verify Python environment setup
- **analyze_kaggle_data.py** - Python script for Kaggle data analysis
- **preview_kaggle_data.py** - Python script for data preview
- **data_preview and analysis.ipynb** - Main analysis notebook (root level)

### **data/** - Data Pipeline
| Subfolder | Purpose |
|-----------|---------|
| **external/** | Third-party raw datasets (Kaggle CSV files) |
| **raw/** | Downloaded data from APIs (NREL, Weather) |
| **processed/** | Cleaned, normalized data ready for warehouse |

### **sql/** - Data Warehouse Layer
| Subfolder | Purpose |
|-----------|---------|
| **ddl/** | CREATE TABLE statements for dimensions & fact tables |
| **dml/** | INSERT, UPDATE, DELETE, and data loading scripts |
| **analytics/** | SELECT queries, aggregations, KPI calculations |

### **src/** - Python ETL Codebase
| Subfolder | Purpose |
|-----------|---------|
| **data_sources/** | API integrations (NREL, OpenWeatherMap) |
| **etl/** | Core ETL pipeline (Extract → Transform → Load) |
| **database/** | Snowflake connection & utilities |
| **analytics/** | KPI & metric calculations |
| **visualization/** | Streamlit dashboards & Plotly charts |

### **docs/** - Documentation
- **data_dictionary.md** - Column definitions & data types
- **schema_ddl.sql** - Complete schema reference

### **tests/** - Quality Assurance
- **test_*.py** - Unit tests for API connections
- **sample_*.csv** - Test data samples

### **reports/** - Output Artifacts
- **data_quality_report.txt** - Analysis findings & data issues
- **numeric_summary.csv** - Statistical summaries
- **sample_data.csv** - Data preview
- **consolidated visual mapping...csv** - Complete schema mapping reference
- **CSV to Table structure.png** - Visual diagram showing CSV to table relationships
- **Data Flow Mapping.png** - Data flow visualization diagram
- **ER Diagram.png** - Entity-relationship diagram for star schema
- **end-to-end project workflow.png** - Complete project workflow visualization

---

## 🔄 Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA SOURCES                              │
├─────────────┬──────────────────────────┬────────────────────┤
│ Kaggle CSV  │ NREL API                 │ OpenWeatherMap API │
└──────┬──────┴──────────────────┬───────┴────────────────────┘
       │                         │
       ▼                         ▼
   [data/external/]         [data/raw/]
   [ev_charging_patterns.csv] [JSON files]
       │                         │
       └──────────────┬──────────┘
                      ▼
        [src/data_sources/*.py]  ◄── Extract from APIs
                      ▼
        [src/etl/transform.py]   ◄── Normalize & clean
                      ▼
        [data/processed/]        ◄── Staging data
                      ▼
        [src/etl/load.py]        ◄── Load to Snowflake
                      ▼
    ┌──────────────────────────────────────┐
    │  SNOWFLAKE DATA WAREHOUSE            │
    ├──────────────────────────────────────┤
    │ Dimensions:                          │
    │  - DIM_USER                          │
    │  - DIM_VEHICLE                       │
    │  - DIM_STATION                       │
    │  - DIM_TIME                          │
    │  - DIM_WEATHER                       │
    │                                      │
    │ Fact Table:                          │
    │  - FACT_CHARGING_SESSIONS            │
    └──────────────────────────────────────┘
                      ▼
        [src/analytics/*.py]    ◄── Analysis & KPIs
                      ▼
    ┌──────────────────────────────────────┐
    │  VISUALIZATION & REPORTING           │
    │  - Streamlit Dashboard               │
    │  - Plotly Charts                     │
    │  - HTML Reports                      │
    └──────────────────────────────────────┘
```

---

## 🎯 Key Components

### **ETL Pipeline** (`src/etl/`)
1. **extract.py** - Fetches data from APIs & files
2. **transform.py** - Normalizes & cleans data
3. **load.py** - Loads into Snowflake
4. **data_quality.py** - Validates data integrity

### **API Integrations** (`src/data_sources/`)
- **nrel_api.py** - Electric vehicle charging stations (National Renewable Energy Lab)
- **weather_api.py** - Weather conditions from OpenWeatherMap

### **Data Warehouse** (`sql/`)
**Star Schema Design:**
- **Fact Table:** FACT_CHARGING_SESSIONS (measures: energy, cost, duration)
- **Dimensions:** Users, Vehicles, Stations, Time, Weather

### **Analysis & Visualization** (`src/analytics/` & `src/visualization/`)
- KPI calculations
- Demand forecasting
- Interactive dashboards

---

## 📊 Star Schema Overview

```
                    ┌─────────────────┐
                    │  FACT_CHARGING  │
                    │    SESSIONS     │
                    └────────┬────────┘
           ┌────────────┬────┴─────┬───────────┬──────────┐
           ▼            ▼          ▼           ▼          ▼
      ┌─────────┐  ┌──────────┐ ┌────────┐ ┌──────┐ ┌──────────┐
      │DIM_USER │  │DIM_TIME  │ │DIM_    │ │DIM_  │ │DIM_     │
      │(user_id)│  │(date_id) │ │STATION │ │VEHI- │ │WEATHER  │
      │         │  │          │ │(sta_id)│ │CLES  │ │(weather │
      │-user_id │  │-date_id  │ │        │ │(veh_ │ │_id)     │
      │-user_typ│  │-year     │ │-station│ │id)   │ │        │
      │-region  │  │-month    │ │-location
      │         │  │-day      │ │-charger│ │-model│ │-temp    │
      └─────────┘  │-dow      │ │-operator
      │        │ │-battery │ │-humidity│
                    │-hour    │ │        │ │-age   │ │        │
                    └──────────┘ └────────┘ └──────┘ └──────────┘

        FACT measures:
        - energy_consumed_kwh
        - charging_cost_usd
        - duration_hours
        - charging_rate_kw
        - start_soc_percent
        - end_soc_percent
```

---
 → data/raw/nrel_stations_*.json
weather_api.fetch_weather()    # Get weather data → data/raw/weather_data_*.json
# Kaggle CSV already in data/external/ev_charging_patterns.csv
```

### **2. Data Analysis** (`data_preview and analysis.ipynb`)
```python
# Analyze data quality, structure, and patterns
# Outputs → reports/ (quality reports, diagrams, summaries)
```

### **3. Data Transformation** (`src/etl/transform.py`)
```python
# Normalize & clean data
transform_ev_sessions()        # Parse timestamps, standardize formats
transform_nrel_stations()      # Extract station attributes
transform_weather_data()       # Process weather information
# Output to data/processed/
```

### **4. Data Quality Checks** (`src/etl/data_quality.py`)
```python
# Validate data integrity
check_nulls()                  # Missing value detection
check_duplicates()             # Find duplicate records
check_referential_integrity()  # Foreign key validation
validate_data_types()          # Type consistency checks
```

### **5. Schema Creation** (`sql/ddl/`)
```sql
-- Create dimension & fact tables in Snowflake
CREATE TABLE DIM_USER...       -- sql/ddl/create_dims.sql
CREATE TABLE FACT_CHARGING...  -- sql/ddl/create_fact_charging.sql
```

### **6. Data Loading** (`src/etl/load.py`)
```python
# Load to Snowflake
load_dimensions()              # DIM_USER, DIM_VEHICLE, DIM_STATION, DIM_TIME, DIM_WEATHER
load_fact_table()              # FACT_CHARGING_SESSIONS
```

### **7. Analysis & Reporting** (`src/analytics/` - future)
```python
# Generate insights & KPIs
calculate_utilization()        # Station usage metrics
forecast_demand()              # Predict future usage
# Export to reports/
```

### **8. Visualization** (`src/visualization/` - future)
```python
# Interactive dashboards
streamlit_dashboard()          # Launch Streamlit app
plotly_charts()               # Generate interactive charts
### **5. Analysis & Reporting** (`src/analytics/`)
```python
# Generate insights & KPIs
calculate_utilization()        # Station usage metrics
forecast_demand()              # Predict future usage
# Export to reports/
```

---

## 🔐 Configuration Files

### **config/api_config.py**
```python
# API keys and endpoints
NREL_API_KEY = "your_key"
WEATHER_API_KEY = "your_key"
SNOWFLAKE_ACCOUNT = "your_account"
```

### **.env** (Git-ignored)
```
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ACCOUNT=
NREL_API_KEY=
WEATHER_API_KEY=
``` & File Locations

| Task | Command/Location |
|------|----------|
| **Run data analysis notebook** | `jupyter notebook "data_preview and analysis.ipynb"` |
| **View project structure** | `cat PROJECT_STRUCTURE.md` |
| **Check all files** | `ls -la` or view this document |
| **View ETL scripts** | `src/etl/` (transform.py, load.py, data_quality.py) |
| **View data warehouse schema** | `sql/ddl/` (create_dims.sql, create_fact_charging.sql) |
| **View API integrations** | `src/data_sources/` (nrel_api.py, weather_api.py) |
| **Check data quality report** | `reports/data_quality_report.txt` |
| **View visualizations** | `reports/*.png` (ER Diagram, Data Flow, etc.) |
| **Test API connections** | `python tests/test_nrel_api.py`, `python tests/test_weather_api.py` |
| **Check Python environment** | `python test_environment.py` |
| **View sample data** | `data/external/ev_charging_patterns.csv` |
| **Check raw API data** | `data/raw/*.json
complete layout)
3. **data_preview and analysis.ipynb** - See actual data analysis & insights
4. **reports/data_quality_report.txt** - Understand data quality issues
5. **reports/*.png** - View visual diagrams (ER Diagram, Data Flow, etc.)
6. **docs/data_dictionary.md** - Column-level data documentation
7. **sql/ddl/*.sql** - Learn the star schema design
8. **src/etl/transform.py** - See data transformation logic
9. **src/data_sources/*.py** - Understand API integrations

---

## 📊 Current Project Status

### ✅ Completed
- Data extraction from APIs (NREL, Weather)
- Kaggle dataset loaded
- Comprehensive data analysis (notebook)
- Star schema design (DDL scripts)
- Data quality assessment
- Visual diagrams & documentation
- ETL transformation logic
- Database connector setup

### 🚧 In Progress / Ready to Implement
- Data loading to Snowflake
- SQL DML scripts (INSERT/UPDATE operations)
- Analytics queries
- Dashboard/visualization layer
- Automated ETL pipeline (Airflow)

### 📁 Empty Folders (Ready for Content)
- `data/processed/` - Will contain cleaned data after ETL
- `sql/dml/` - For INSERT/UPDATE/DELETE scripts
- `sql/analytics/` - For analytical queries
- `src/analytics/` - For KPI calculation functions
- `src/visualization/` - For Streamlit dashboard
- `notebooks/` - For additional exploratory notebooks

---

**Last Updated:** January 30, 2026  
**Project Type:** Data Warehouse (Star Schema)  
**Tech Stack:** Python, Snowflake, SQL, Jupyter, Pandas, Streamlit  
**Total Files:** 30+ (excluding virtual environment)
- Generated from the analysis notebook
- Contains missing value analysis
- Documents data cleaning requirements

---

## 💡 Common Tasks

| Task | Location |
|------|----------|
| Run data analysis | `jupyter notebook data_preview\ and\ analysis.ipynb` |
| Check ETL status | `src/etl/*.py` |
| View data warehouse schema | `sql/ddl/*.sql` |
| View API integrations | `src/data_sources/*.py` |
| Check data quality | `reports/data_quality_report.txt` |
| Launch dashboard | `src/visualization/streamlit_app.py` |

---

## 📖 Reading Order (For New Team Members)

1. **README.md** - Project overview & goals
2. **PROJECT_STRUCTURE.md** - This file (understand layout)
3. **data_preview and analysis.ipynb** - See actual data insights
4. **docs/data_dictionary.md** - Understand the data
5. **sql/ddl/*.sql** - Learn the schema
6. **src/etl/transform.py** - See data transformation logic
7. **src/data_sources/*.py** - Understand data integrations

---

**Last Updated:** January 30, 2026  
**Project Type:** Data Warehouse (Star Schema)  
**Tech Stack:** Python, Snowflake, SQL, Jupyter, Pandas
