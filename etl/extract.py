import pandas as pd
from sqlalchemy import create_engine

def load_csv(file_path):
    return pd.read_csv(file_path)


def load_from_postgres(connection_string, query):
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df