-- FACT_CHARGING_SESSIONS DDL
CREATE OR REPLACE TABLE ANALYTICS.FACT_CHARGING_SESSIONS (
    session_id STRING PRIMARY KEY,
    user_id INTEGER,
    station_id STRING,
    date_id INTEGER,
    start_timestamp TIMESTAMP_LTZ,
    end_timestamp TIMESTAMP_LTZ,
    energy_consumed_kwh FLOAT,
    duration_hours FLOAT,
    charging_rate_kw FLOAT,
    charging_cost_usd FLOAT,
    distance_driven_km FLOAT,
    start_soc_percent INTEGER,
    end_soc_percent INTEGER
);

-- DIMENSION TABLE DDLS...
