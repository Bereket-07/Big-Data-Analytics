import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Load data
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/cleaned_amazon_data.csv"))
amazon_df = pd.read_csv(file_path)

# PostgreSQL Connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

# ✅ Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS amazon_data_table (
        id SERIAL PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        price NUMERIC,
        rating NUMERIC,
        sales INTEGER
    );
""")
conn.commit()

# ✅ Insert data into PostgreSQL
for _, row in amazon_df.iterrows():
    cursor.execute(
        """
        INSERT INTO amazon_data_table (product_name, category, price, rating, sales)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row["title"],  # Product Name
            row["categoryname"],  # Category
            row["price"],  # Price
            row["stars"],  # Rating
            row["boughtinlastmonth"]  # Sales
        )
    )

conn.commit()
cursor.close()
conn.close()
print("✅ Data inserted successfully!")
