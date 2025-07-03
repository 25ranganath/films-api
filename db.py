import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Database connection established.")
    return conn
