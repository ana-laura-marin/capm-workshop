from __future__ import annotations
import os
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.environ["POSTGRES_HOST"]
    db = os.environ["BONDS_DB"]
    return create_engine(f"postgresql://{user}:{password}@{host}:5432/{db}")

def fetch_risk_free_rate() -> pd.DataFrame:
    engine = get_engine()
    query = text("""
        SELECT observation_date, value::float AS rate
        FROM bronze.fred_observations
        WHERE series_id = 'GS10'
          AND value != '.'
        ORDER BY observation_date
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    df["observation_date"] = pd.to_datetime(df["observation_date"])
    return df

def fetch_hy_spread() -> pd.DataFrame:
    engine = get_engine()
    query = text("""
        SELECT observation_date, value::float AS spread
        FROM bronze.fred_observations
        WHERE series_id = 'BAMLH0A0HYM2'
          AND value != '.'
        ORDER BY observation_date
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    df["observation_date"] = pd.to_datetime(df["observation_date"])
    return df
