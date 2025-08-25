

-- 1. User Dimension
CREATE OR REPLACE TABLE ANALYTICS.DIM_USER (
  user_id    INTEGER    NOT NULL PRIMARY KEY,  -- Surrogate key from CSV User ID
  user_type  STRING     NOT NULL               -- Category of user (Commuter, Casual, etc.)
);

-- 2. Vehicle Dimension
CREATE OR REPLACE TABLE ANALYTICS.DIM_VEHICLE (
  vehicle_id            STRING   NOT NULL PRIMARY KEY,  -- Surrogate key (Vehicle Model)
  vehicle_model         STRING   NOT NULL,              -- Name of the vehicle model
  battery_capacity_kwh  FLOAT    NOT NULL,              -- Battery capacity in kWh
  vehicle_age_years     FLOAT    NOT NULL               -- Vehicle age in years
);

-- 3. Station Dimension
CREATE OR REPLACE TABLE ANALYTICS.DIM_STATION (
  station_id       STRING  NOT NULL PRIMARY KEY,  -- Unique station identifier
  station_location STRING  NOT NULL,              -- City or full address
  charger_type     STRING  NOT NULL,              -- Connector type (Level 1, 2, DCFC)
  network_operator STRING  NULL                   -- Station operator or network provider
);

-- 4. Time Dimension
CREATE OR REPLACE TABLE ANALYTICS.DIM_TIME (
  date_id     INTEGER    NOT NULL PRIMARY KEY, -- Surrogate key for date-hour
  date_value  DATE       NOT NULL,             -- Calendar date
  year        INTEGER    NOT NULL,
  month       INTEGER    NOT NULL,
  day         INTEGER    NOT NULL,
  weekday     STRING     NOT NULL,             -- e.g., Monday
  hour        INTEGER    NOT NULL,             -- 0–23
  time_of_day STRING     NOT NULL              -- Morning/Afternoon/Evening
);

-- 5. Weather Dimension
CREATE OR REPLACE TABLE ANALYTICS.DIM_WEATHER (
  weather_id          INTEGER    NOT NULL PRIMARY KEY, -- Surrogate key per record
  date_id             INTEGER    NOT NULL,             -- FK to DIM_TIME.date_id
  temperature_celsius FLOAT      NOT NULL,             -- Ambient temperature
  humidity_percent    FLOAT      NOT NULL,             -- Relative humidity
  weather_main        STRING     NOT NULL,             -- e.g., Clear, Rain
  CONSTRAINT fk_time_weather
    FOREIGN KEY(date_id) REFERENCES ANALYTICS.DIM_TIME(date_id)
);
