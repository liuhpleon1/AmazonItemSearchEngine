from UserDBsetup import User,base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()
class DBsearch:
    def __init__(self,input_name,input_password):
        self.input_name = input_name
        self.input_password = input_password
        
    def search_user(self):
        user = ""
        try:
            user = session.query(User).filter_by(name = self.input_name).one()
            print user
        except:
            return False
        if user == "": 
            return False
        elif user.password!=self.input_password:
            return False
        else:
            return True