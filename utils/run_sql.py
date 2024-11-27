import os
from snowflake_connector import get_snowflake_connection

def execute_sql_file(file_path):
    with open(file_path, 'r') as sql_file:
        query = sql_file.read()
    
    conn = get_snowflake_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            print(f"Executed {file_path} successfully")
    finally:
        conn.close()

if __name__ == "__main__":
    file_path = os.getenv("SQL_FILE_PATH")  # Pass the file path as an environment variable
    execute_sql_file(file_path)
