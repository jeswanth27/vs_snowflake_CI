import os
import snowflake.connector

def connect_to_snowflake():
    try:
        # Establish the connection
        conn = snowflake.connector.connect(
            user="jeswanthedubilli",  # Replace with your Snowflake username
            password="Gss@1234",     # Replace with your Snowflake password
            account="pe39761.ap-southeast-1",  # Replace with your Snowflake account
            warehouse="COMPUTE_WH",  # Replace with your warehouse name
            database="task_db",      # Replace with your database name
            schema="task_schema"
        )
        print("Connection successful!")
        # Execute a test query
        cur = conn.cursor()
        cur.execute("SELECT CURRENT_VERSION()")
        result = cur.fetchone()
        print(f"Snowflake Version: {result[0]}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_to_snowflake()
