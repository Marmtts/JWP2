from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData
from sqlalchemy import inspect
import sqlalchemy as db
from sqlalchemy import (
    Table, 
    Column, 
    String,
    Integer, 
    Float,
    Boolean,
    select,
    text,
    func
)


engine = create_engine('sqlite:///census.sqlite')
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

connection = engine.connect()
print(connection)

metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)
print(repr(census))

stmt = text('SELECT DISTINCT state FROM census')  
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results[:])

stmt = text('SELECT state, SUM(pop2000) FROM census WHERE state = "Alaska" OR state = "New York" GROUP BY(state) ')  
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results[:])

stmt = text('SELECT state, SUM(pop2008) FROM census WHERE state = "Alaska" OR state = "New York" GROUP BY(state)')  
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results[:])

stmt = text('SELECT sex, SUM(pop2008) FROM census WHERE state = "New York" GROUP BY(sex)')  
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results[:])

