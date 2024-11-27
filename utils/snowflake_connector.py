import snowflake.connector
import os

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        #user=os.getenv("SNOWFLAKE_USER"),
        #password=os.getenv("SNOWFLAKE_PASSWORD"),
        #account=os.getenv("SNOWFLAKE_ACCOUNT"),
        #warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        #database=os.getenv("SNOWFLAKE_DATABASE"),
        #schema=os.getenv("SNOWFLAKE_SCHEMA")

        user="jeswanthedubilli",  # Replace with your Snowflake username
            password="Gss@1234",     # Replace with your Snowflake password
            account="pe39761.ap-southeast-1",  # Replace with your Snowflake account
            warehouse="COMPUTE_WH",  # Replace with your warehouse name
            database="task_db",      # Replace with your database name
            schema="task_schema"
    )
    return conn
