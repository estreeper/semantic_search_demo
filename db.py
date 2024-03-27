import psycopg2
import os

def create_conn():
    conn = psycopg2.connect(
        dbname='news_search',
        user='postgres',
        host='localhost',
        port='5432'
    )
    return conn
