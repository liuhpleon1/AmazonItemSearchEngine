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
        
    def check_user(self):
        user = ""
        try:
            user = session.query(User).filter_by(name = self.input_name).one()
            print user
        except:
            return [False,False]
        if user == "": 
            return [False,False]
        elif user.password!=self.input_password:
            return [True,False]
        else:
            return [True,True]
    
    def search_user(self):
        try:
            user = session.query(User).filter_by(name = self.input_name).one()
            password = user.password
            print user.password
            return password
        except:
            return None
        
    def search_email(self,email):
        try:
            user = session.query(User).filter_by(email = email).one()
            username = user.username
            password = user.password
            print user.password
            return [username,password]
        except:
            return None
        
    def search_cellphone(self,cellphone):
        try:
            user = session.query(User).filter_by(phone = cellphone).one()
            username = user.username
            password = user.password
            print user.password
            return [username,password]
        except:
            return None
        
    def get_info(self):
        try:
            user = session.query(User).filter_by(name = self.input_name).one()
            name = user.name.__str__()
            password = user.password.__str__()
            email = user.email.__str__()
            cellphone = user.phone.__str__()
            item = user.item.__str__()
            dict = {"username":name,"password":password,"email":email,"cellphone":cellphone,"item":item}
            return dict
        except:
            return None
