from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData,Date
from sqlalchemy.exc import OperationalError
from sqlalchemy_utils import database_exists, create_database
import csv
from sqlalchemy import insert
from datetime import datetime, date


###engine = create_engine('sqlite:///task.db', echo=True)
meta = MetaData()

engine = create_engine('sqlite:///task5.db')
conn = engine.connect()

if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))

                
clean_stations=Table(
    'clean_stations', meta,
    Column('station', String, primary_key=True),
    Column('latitude',Integer),
    Column('longitude',Integer),
    Column('elevantion',Integer),
    Column('name',String),
    Column('country',String),
    Column('state',String),
)



clean_measure=Table(
    'clean_measure', meta,
    Column('station', String),
    Column('date',Date),
    Column('precip',Integer),
    Column('tobs',Integer),
)

meta.create_all(engine)
print(engine.table_names())



with open('clean_stations.csv', 'r') as csvfile:
    tbl_reader = csv.reader(csvfile, delimiter=',')
    next(tbl_reader, None)
    for c in tbl_reader:  
        stmt = insert(clean_stations).values(station=c[0], latitude=c[1],longitude=c[2], elevantion=c[3], name=c[4], country=c[5], state=c[6])
        with engine.connect() as conn:
            result = conn.execute(stmt)



with open('clean_measure.csv', 'r') as csvfile:
    tbl_reader = csv.reader(csvfile, delimiter=',')
    next(tbl_reader, None)
    for c in tbl_reader:
        stmt = insert(clean_measure).values(station=c[0], date=datetime.strptime(c[1],"%Y-%m-%d"),precip=c[2], tobs=c[3])
        with engine.connect() as conn:
            result = conn.execute(stmt)

print(stmt)
with engine.connect() as conn:
     result = conn.execute(stmt)

conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

conn.close()
