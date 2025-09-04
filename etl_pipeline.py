import pandas as pd
from sqlalchemy import create_engine
import logging

# Setup logging (writes to etl_log.txt in same folder)
logging.basicConfig(
    filename="etl_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_etl():
    try:
        logging.info("ETL Job Started")

        # 1. Extract
        df = pd.read_csv("C:/Users/monda/Documents/Data_engineering_projects/incoming_data/movies_sample.csv", sep=";", encoding="ISO-8859-1")
        logging.info(f"Extracted {len(df)} rows from CSV")

        # 2. Transform
        df['released'] = pd.to_datetime(df['released'], errors='coerce')
        df['budget'] = df['budget'].fillna(0).astype(int)
        df['gross'] = df['gross'].fillna(0).astype(int)
        df['company'] = df['company'].fillna("Unknown")
        df['country'] = df['country'].fillna("Unknown")
        df = df.dropna(subset=['name'])
        logging.info("Data transformation completed")

        # 3. Load into MySQL
        engine = create_engine("mysql+mysqlconnector://root:root@localhost/movies_db")
        df.to_sql("movies_data", con=engine, if_exists="append", index=False)
        logging.info(f"Loaded {len(df)} rows into MySQL")

        logging.info("ETL Job Completed Successfully")

    except Exception as e:
        logging.error(f"ETL Job Failed: {e}")

if __name__ == "__main__":
    run_etl()
