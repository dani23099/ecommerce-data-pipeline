import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

print("Initiating Data Load (ETL - Load Phase)...")

# 1. Read clean dataset
df = pd.read_csv("ecommerce_data.csv")

# 2. Configure the database connection
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")
db_host = 'localhost'
db_name = 'ecommerce_analytics'

# Create the connection
conexion = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(conexion)

print("Establishing secure connection to MariaDB...")

# 3. Load the data into 'inventory' table
try:

    df.to_sql(name='inventory', con=engine, if_exists='append', index=False)
    print("🚀 All products are securely stored in the database.")
except Exception as e:
    print(f"Error loading data: {e}")