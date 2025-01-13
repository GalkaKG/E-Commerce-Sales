# from sqlalchemy import create_engine

# table_name = 'amazon_sales_report'

# def load_to_postgres():
#     connection_string = 'postgresql+psycopg2://postgres:postgres@postgres:5432/ecommerce'
#     engine = create_engine(connection_string)
    
#     return table_name, engine

# def load_to_postgres_from_local():
#     connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerce'
#     engine = create_engine(connection_string)
    
#     return table_name, engine


from sqlalchemy import create_engine

table_name = 'amazon_sales_report'

def load_to_postgres(host='postgres'):
    # Default to 'localhost', but you can change it to 'postgres' or any other host when calling
    connection_string = f'postgresql+psycopg2://postgres:postgres@{host}:5432/ecommerce'
    engine = create_engine(connection_string)
    
    return table_name, engine
