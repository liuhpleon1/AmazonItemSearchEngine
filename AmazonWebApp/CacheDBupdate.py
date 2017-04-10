from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from CacheDBsetup import Cache,base
engine = create_engine('sqlite:///cache.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()
class Update:
    def __init__(self,query):
        self.query = query
    def add(self):
        try:
            instance = session.query(Cache).filter_by(query = self.query).one()
            instance.id = instance.id+1
            session.add(instance)
            session.commit()
        except:
            new_query = Cache(id=1,query=self.query)
            session.add(new_query)
            session.commit()
            
    def forward(self):
        val = {}
        for instance in session.query(Cache).order_by(Cache.id):
            val[instance.query.__str__()] = instance.id
        val= sorted(val.iteritems(), key=lambda d:d[1], reverse = True)
        return val  