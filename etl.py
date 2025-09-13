import pandas as pd
from sqlalchemy import create_engine
from constants import mysql_uri

def load_sales_data(df):
    engine = create_engine(mysql_uri)
    df.to_sql('sales', engine, if_exists='replace', index=False)
