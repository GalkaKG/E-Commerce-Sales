from sqlalchemy import create_engine

def load_to_postgres(df):
    connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerce'
    engine = create_engine(connection_string)
    
    df.to_sql('amazon_sales_report', engine, index=False, if_exists='replace')  
