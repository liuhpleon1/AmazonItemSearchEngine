from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
from _mysql import NULL
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()
class DBregister():
    def __init__(self,input_name,input_password,input_email,input_phone):
        self.input_name = input_name
        self.input_password = input_password
        self.input_email = input_email
        self.input_phone = input_phone
        
    def register_user(self):
        usercheck = [True,True,True]
        try:
            session.query(User).filter_by(name=self.input_name).one() 
        except:
            usercheck[0] = False
        try:      
            session.query(User).filter_by(email=self.input_email).one()     
        except:
            usercheck[1] = False
        try:
            session.query(User).filter_by(phone=self.input_phone).one()  
        except:
            usercheck[2] = False
            
        if(usercheck[0]==False and usercheck[1]==False and usercheck[2]==False):
            print usercheck
            newuser = User(name=self.input_name,password=self.input_password,email = self.input_email,phone=self.input_phone)
            session.add(newuser)
            session.commit()
        else:
            print 'exist'
        return usercheck
