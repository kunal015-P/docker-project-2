import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="ecommerce",
        user="admin",
        password="admin"
    )
    return conn
