import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df , table_name , engine):
    '''this function would ingest dataframe into database table'''
    df.to_sql(table_name , con = engine , if_exists = 'replace', index = False)
    
def load_raw_data():
    '''this function would load csv as dataframe and insert into database'''
    st_time = time.time()
    for file in os.listdir('data'):
        if file.endswith(".csv"):
            try:
                df = pd.read_csv(os.path.join("data", file))
                ingest_db(df, file[:-4], engine)
                logging.info(f"Ingested {file}")
            except Exception as e:
                logging.error(f"Failed to ingest {file}: {e}")
    ed_time = time.time()
    logging.info("ingestion Completed")
    total_time = (ed_time - st_time)/60
    logging.info(f"total time taken is {total_time} minutes")

if __name__ == '__main__':
    load_raw_data()