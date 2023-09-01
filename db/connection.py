import pyodbc 
from sqlalchemy import create_engine
from urllib.parse import quote_plus


def conn_engine():
    conn_str = ("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=DELL;"
                        "Database=DATA_IMPACTA;"
                        "Trusted_Connection=yes;")

    url_db = quote_plus(conn_str)
    engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)
    
    return engine
