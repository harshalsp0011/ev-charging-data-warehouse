# EV Charging Network Data Warehouse

A cloud-based data warehouse using Snowflake for EV charging station analytics, focusing on optimization and demand forecasting in the electric vehicle ecosystem.

---

## Project Overview

This project builds a scalable data warehouse to analyze EV charging patterns, station utilization, and demand forecasting using modern cloud technologies. The system processes charging session data, weather information, and station metadata to provide actionable insights for charging network optimization.

**Domain**: Electric Vehicles / Smart Mobility  
**Technology Stack**: Python, Snowflake, Apache Airflow, Streamlit  
**Duration**: 18–24 weeks  
**Resources**: Free tiers and student accounts only

---

## Key Features

- **Real-time Data Processing**: Automated ETL pipelines for charging session, station, and weather data  
- **Star Schema Design**: Optimized fact and dimension tables in Snowflake  
- **Predictive Analytics**: Demand forecasting and utilization analysis  
- **Interactive Dashboards**: Streamlit-based visualization platform  
- **Weather Integration**: Correlate weather with charging patterns  
- **Cost Optimization**: Free and student-friendly implementation

---

## Tech Stack

| Component       | Technology                  | Purpose                                           |
|-----------------|-----------------------------|---------------------------------------------------|
| Data Warehouse  | Snowflake (Student Trial)   | Cloud-based data storage and processing           |
| ETL Pipeline    | Python, Apache Airflow      | Data extraction, transformation, loading          |
| Analytics       | Python (pandas, NumPy)      | Statistical analysis and calculations             |
| Visualization   | Streamlit, Plotly           | Interactive dashboards and charts                 |
| Data Sources    | Kaggle CSV, NREL API, OpenWeatherMap API | Raw session, station, and weather data |
| Development     | VS Code, Jupyter            | Code development and exploration                  |

---

## Project Structure

ev-charging-data-warehouse/

├── src/

│ ├── data_sources/ # API integrations (NREL, OpenWeatherMap)

│ ├── etl/ # Extract, Transform, Load scripts

│ ├── database/ # Snowflake connection utilities

│ ├── analytics/ # KPI calculations and analysis

│ └── visualization/ # Streamlit dashboard code

├── config/ # Configuration files (.env templates)

├── sql/

│ ├── ddl/ # Schema creation scripts

│ ├── dml/ # Data manipulation scripts

│ └── analytics/ # Analytical queries

├── tests/ # Unit and integration tests

├── docs/ # Project documentation

├── notebooks/ # Jupyter notebooks for exploration

├── data/

│ ├── raw/ # Downloaded CSV/JSON files

│ ├── external/ # Reference datasets (Kaggle)

│ └── processed/ # Transformed CSVs for loading

└── logs/ # Application and ETL logs



---

## Getting Started

### Prerequisites

- Python 3.8+  
- Snowflake account (student trial)  
- Git

### Installation & Setup

1. Clone the repository  

git clone https://github.com/yourusername/ev-charging-data-warehouse.git
cd ev-charging-data-warehouse

2. Create and activate a Python virtual environment  

python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows

3. Install dependencies  

pip install -r requirements.txt


4. Configure environment variables  
- Copy `.env.example` to `.env`  
- Add your Snowflake, OpenWeatherMap, and NREL API keys

---

## Data Sources & Attributes

### CSV (ev_charging_patterns.csv)

| Attribute                                     | Description                                 |
|-----------------------------------------------|---------------------------------------------|
| User ID                                       | Unique user identifier                      |
| Vehicle Model                                 | EV model name                               |
| Battery Capacity (kWh)                        | Battery capacity                            |
| Charging Station ID                           | Station identifier                          |
| Charging Station Location                     | City or address                             |
| Charging Start Time / End Time                | Session timestamps                          |
| Energy Consumed (kWh)                         | Energy delivered                            |
| Charging Duration (hours)                     | Session duration                            |
| Charging Rate (kW)                            | Power rate                                  |
| Charging Cost (USD)                           | Session cost                                |
| Time of Day, Day of Week                      | Derived time attributes                     |
| State of Charge (Start % / End %)             | Battery SOC at start/end                    |
| Distance Driven (km)                          | Distance since last charge                  |
| Temperature (°C)                              | Recorded weather (session location)         |
| Vehicle Age (years)                           | Age of vehicle                              |
| Charger Type                                  | Level 1, Level 2, DC Fast                   |
| User Type                                     | Commuter, Casual, Long-Distance             |

### NREL API (nrel_stations.json)

| Attribute             | Description                       |
|-----------------------|-----------------------------------|
| station_id            | Unique station identifier         |
| station_name, address | Station name and street address   |
| city, state, zip      | Location details                  |
| ev_connector_types    | Supported connector types         |
| station_operator      | Network or operator name          |

### OpenWeatherMap API (weather_data.json)

| Attribute       | Description                  |
|-----------------|------------------------------|
| dt (timestamp)  | UNIX date-time               |
| main.temp       | Temperature (°C)             |
| main.humidity   | Humidity (%)                 |
| weather[0].main | Weather condition (e.g., Clear) |
| wind.speed, deg | Wind speed and direction     |

---

## Completed Tasks & Roadmap

| Task   | Description                                        | Status         |
|--------|----------------------------------------------------|----------------|
| 1      | Project Initialization                             | ✅ Completed   |
| 2      | Python Environment Setup & Dependencies            | ✅ Completed   |
| 3      | Free Service Registration (Snowflake, APIs)        | ✅ Completed   |
| 4      | Data Acquisition & Profiling (CSV, NREL, Weather)  | ✅ Completed   |
| 5      | Star Schema Design & DDL Creation                  | ☐ In Progress  |
| 6      | ETL Pipeline Development                           | ☐ Upcoming     |
| 7      | Synthetic Data Generation                          | ☐ Upcoming     |
| 8      | Snowflake Performance Optimization                 | ☐ Upcoming     |
| 9      | Analytics Script & KPI Development                 | ☐ Upcoming     |
| 10     | Dashboard Creation & Deployment                    | ☐ Upcoming     |
| 11     | Monitoring, Testing & Reporting                    | ☐ Upcoming     |

---

## Next Steps (Task 5)

1. Review profiling reports under `reports/`  
2. Define primary/foreign keys and surrogate key strategy  
3. Draft and finalize DDL scripts in `sql/ddl/`  
4. Execute DDL in Snowflake and validate table structures  

---

## Contributing

1. Fork the repository  
2. Create a feature branch  
3. Add or update code/docs  
4. Submit a pull request  

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Developed by Harshal Patil (harshal.sanjivpatil2000@gmail.com) as part of a data engineering portfolio.*  
