CREATE OR REPLACE TABLE ANALYTICS.FACT_CHARGING_SESSIONS (
  session_id              STRING        PRIMARY KEY,
  user_id                 INTEGER       NOT NULL,
  station_id              STRING        NOT NULL,
  vehicle_id              STRING        NOT NULL,
  date_id                 INTEGER       NOT NULL,
  weather_id              INTEGER       NOT NULL,
  start_timestamp         TIMESTAMP_LTZ NOT NULL,
  end_timestamp           TIMESTAMP_LTZ NOT NULL,
  energy_consumed_kwh     FLOAT         NULL,
  duration_hours          FLOAT         NOT NULL,
  charging_rate_kw        FLOAT         NULL,
  charging_cost_usd       FLOAT         NOT NULL,
  distance_driven_km      FLOAT         NULL,
  start_soc_percent       INTEGER       NOT NULL,
  end_soc_percent         INTEGER       NOT NULL,
  CONSTRAINT fk_user
    FOREIGN KEY(user_id) REFERENCES ANALYTICS.DIM_USER(user_id),
  CONSTRAINT fk_station
    FOREIGN KEY(station_id) REFERENCES ANALYTICS.DIM_STATION(station_id),
  CONSTRAINT fk_vehicle
    FOREIGN KEY(vehicle_id) REFERENCES ANALYTICS.DIM_VEHICLE(vehicle_id),
  CONSTRAINT fk_time
    FOREIGN KEY(date_id) REFERENCES ANALYTICS.DIM_TIME(date_id),
  CONSTRAINT fk_weather
    FOREIGN KEY(weather_id) REFERENCES ANALYTICS.DIM_WEATHER(weather_id)
);
COMMENT = 'Fact table capturing EV charging session details including user, station, vehicle, time, weather, energy consumed, duration, cost, and state of charge.';