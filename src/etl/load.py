from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from database.snowflake_connector import get_connection

RAW_STAGE = '@RAW_DATA.EXT_STAGE'
PROCESSED   = Path('data/processed')
FILES = {
    'ev_sessions':   PROCESSED / 'ev_sessions_transformed.csv',
    'nrel_stations': PROCESSED / 'nrel_stations_transformed.csv',
    'weather_data':  PROCESSED / 'weather_transformed.csv'
}

def main():
    conn = get_connection()
    cs = conn.cursor()
    
    try:
        # Set database and schema context first
        cs.execute("USE DATABASE EV_CHARGING_DW")
        cs.execute("USE SCHEMA RAW_DATA")
        cs.execute("USE WAREHOUSE EV_DEV_WH")
        
        # PUT files into stage
        for name, path in FILES.items():
            put_cmd = f"PUT file://{path.absolute()} {RAW_STAGE}/{path.name} OVERWRITE = TRUE"
            print(f"Executing: {put_cmd}")
            cs.execute(put_cmd)
        
        # COPY INTO staging tables
        copy_commands = [
            f"""
            COPY INTO STAGING.stg_ev_sessions
            FROM {RAW_STAGE}/ev_sessions_transformed.csv
            FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
            ON_ERROR = 'CONTINUE'
            """,
            f"""
            COPY INTO STAGING.stg_nrel_stations  
            FROM {RAW_STAGE}/nrel_stations_transformed.csv
            FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
            ON_ERROR = 'CONTINUE'
            """,
            f"""
            COPY INTO STAGING.stg_weather
            FROM {RAW_STAGE}/weather_transformed.csv
            FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
            ON_ERROR = 'CONTINUE'
            """
        ]
        
        for cmd in copy_commands:
            print(f"Executing COPY command...")
            cs.execute(cmd)
            
        conn.commit()
        print("Data loaded into Snowflake STAGING schema successfully!")
        
    except Exception as e:
        print(f"Error during load: {e}")
        conn.rollback()
        raise
    finally:
        cs.close()
        conn.close()

if __name__ == '__main__':
    main()
