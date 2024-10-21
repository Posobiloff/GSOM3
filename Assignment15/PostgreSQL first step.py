import os
import json
import psycopg2
from psycopg2.extras import DictCursor
POSTGRESQL_HOST = '10.129.0.25'
#1. Close connection and cursor manually
!env | grep POST
conn = psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
)
cur = conn.cursor()

query = 'SELECT airport_name, city FROM airports'
cur.execute(query)
records = cur.fetchall()
cur.close()
conn.close()
records

query = 'SELECT model FROM aircrafts'
cur.execute(query)
records = cur.fetchall()
cur.close()
conn.close()
records

query = 'SELECT passenger_name, ticket_no FROM Tickets'
cur.execute(query)
records = cur.fetchall()
records

#2. Usage of "with" in the context manager
with psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT city, coordinates FROM Airports')
        records = cur.fetchall()
records

with psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT aircraft_code, range FROM Aircrafts')
        records = cur.fetchall()
records

with psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT flight_id, status FROM Flights')
        records = cur.fetchall()
records

#3. Usage of IPhyton SQL
!pip install ipython-sql

%load_ext sql
!env | grep POST
import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'
CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)

%%sql $CONNECT_DATA
    SELECT airport_name, coordinates FROM Airports
    
%sql SELECT airport_name, timezone FROM Airports

%sql SELECT aircraft_code, model, range FROM Aircrafts