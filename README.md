# EV Charging Network Data Warehouse

A cloud-based data warehouse using Snowflake for EV charging station analytics, focusing on optimization and demand forecasting in the electric vehicle ecosystem.

## Project Overview

This project builds a scalable data warehouse to analyze EV charging patterns, station utilization, and demand forecasting using modern cloud technologies. The system processes real-time charging session data, weather information, and station metadata to provide actionable insights for charging network optimization.

**Domain**: Electric Vehicles / Smart Mobility  
**Technology Stack**: Python, Snowflake, Apache Airflow, Streamlit  
**Duration**: 18-24 weeks  
**Resources**: Free tiers and student accounts only

## Key Features

- **Real-time Data Processing**: Automated ETL pipelines for charging session data
- **Star Schema Design**: Optimized data warehouse architecture
- **Predictive Analytics**: Demand forecasting and utilization analysis
- **Interactive Dashboards**: Streamlit-based visualization platform
- **Weather Integration**: Weather impact analysis on charging patterns
- **Cost Optimization**: Free and student-friendly implementation

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Data Warehouse | Snowflake (Student Trial) | Cloud-based data storage and processing |
| ETL Pipeline | Python, Apache Airflow | Data extraction, transformation, loading |
| Analytics | Python (Pandas, NumPy) | Statistical analysis and calculations |
| Visualization | Streamlit, Plotly | Interactive dashboards and charts |
| Data Sources | NREL API, OpenWeatherMap | EV station data and weather information |
| Development | VS Code, Jupyter | Code development and exploration |

## Project Structure

ev-charging-data-warehouse/

├── src/

│ ├── data_sources/ # API integrations and data collection

│ ├── etl/ # Extract, Transform, Load processes

│ ├── database/ # Snowflake connection and schema

│ ├── analytics/ # KPI calculations and analysis

│ └── visualization/ # Dashboard and reporting

├── config/ # Configuration files

├── sql/ # SQL scripts for database operations

│ ├── ddl/ # Data Definition Language

│ ├── dml/ # Data Manipulation Language

│ └── analytics/ # Analytical queries

├── tests/ # Unit and integration tests

├── docs/ # Project documentation

├── notebooks/ # Jupyter notebooks for exploration

├── data/ # Local data storage

│ ├── raw/ # Unprocessed data

│ ├── processed/ # Cleaned data

│ └── external/ # Third-party datasets

└── logs/ # Application logs



## Getting Started

### Prerequisites
- Python 3.8+
- Snowflake account (student trial available)
- Git or GitHub Desktop

### Installation
1. Clone the repository
2. Set up virtual environment
3. Install dependencies from requirements.txt
4. Configure API keys and database connections

### Quick Start
Clone the repository
git clone https://github.com/yourusername/ev-charging-data-warehouse.git

Navigate to project directory
cd ev-charging-data-warehouse

Create virtual environment
python -m venv ev_env

Activate virtual environment
source ev_env/bin/activate # Linux/Mac

or
ev_env\Scripts\activate # Windows

Install dependencies
pip install -r requirements.txt



## Data Sources

### Primary Data Sources
- **NREL Alternative Fuels Data Center**: Comprehensive US/Canada charging stations
- **OpenWeatherMap API**: Historical and forecast weather data
- **Kaggle EV Datasets**: Sample charging session data for development

### Synthetic Data Generation
- **Python Libraries**: Generate realistic charging patterns using Faker, NumPy
- **Sample Datasets**: Create test data for development and validation

## Key Metrics & KPIs

- **Station Utilization Rate**: Usage patterns and efficiency metrics
- **Peak Demand Analysis**: High-traffic periods and congestion identification
- **Revenue Analytics**: Cost optimization and pricing strategy insights
- **Fault Detection**: Automated identification of station performance issues
- **Weather Impact**: Correlation between weather and charging behavior

## Development Phases

1. **Project Setup**: Environment configuration and tool setup
2. **Data Integration**: API connections and data collection
3. **ETL Pipeline**: Data processing and transformation
4. **Data Warehouse**: Snowflake schema design and implementation
5. **Analytics**: KPI calculations and business intelligence
6. **Visualization**: Dashboard creation and reporting
7. **Testing**: Quality assurance and validation
8. **Deployment**: Production deployment and monitoring

## Free Resources Used

- **Snowflake**: Student trial (120 days, $400 credits)
- **OpenWeatherMap**: Free tier (1,000 calls/day)
- **NREL API**: Free with registration
- **Streamlit**: Community Cloud hosting
- **GitHub**: Free repository and Actions
- **Python**: Open source with extensive libraries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NREL for providing comprehensive EV charging station data
- Snowflake University for educational resources
- OpenWeatherMap for weather data integration
- Open source community for tools and libraries

## Contact

**Project Developer**: Harshal Patil
**Email**: harshal.sanjivpatil2000@gmail.com  


---

*This project is developed as part of a data engineering portfolio, demonstrating skills in cloud data warehousing, ETL processes, and analytics visualization.*
