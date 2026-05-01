import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def upload_data(file_path, table_name):
    try:
        df = pd.read_csv(file_path)
        
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Success: '{table_name}' table created and data uploaded.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    upload_data('data/StudentPerformanceFactors.csv', 'my_table')