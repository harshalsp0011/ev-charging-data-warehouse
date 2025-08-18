import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

ACCOUNT  = os.getenv('SNOWFLAKE_ACCOUNT')
USER     = os.getenv('SNOWFLAKE_USER')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
ROLE     = os.getenv('SNOWFLAKE_ROLE', 'SYSADMIN')

def get_connection():
    return snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        role=ROLE,
        client_session_keep_alive=True
    )


def execute_queries(conn, queries):
    cs = conn.cursor()
    try:
        for q in queries:
            cs.execute(q)
        conn.commit()
    finally:
        cs.close()
