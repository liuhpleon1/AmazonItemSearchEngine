from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

base = declarative_base()

class Cache(base):
    __tablename__ = 'cache'
    id = Column(Integer,nullable = False)
    query = Column(String(40),nullable = False,primary_key=True)
    
engine = create_engine('sqlite:///cache.db')
base.metadata.create_all(engine)
