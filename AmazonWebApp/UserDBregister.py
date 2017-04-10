from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
import json
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
            newuser = User(name=self.input_name,password=self.input_password,email = self.input_email,phone=self.input_phone,item="{}")
            session.add(newuser)
            session.commit()
        else:
            print 'exist'
        return usercheck

class DBupdate():
    def __init__(self,username):
        self.username = username;
    def update_user(self,password,email,cellphone):
        name = session.query(User).filter_by(name=self.username).one()
        if password != '':
            name.password = password
        if email != '':
            name.email = email
        if cellphone!='':
            name.phone = cellphone
        session.add(name)
        session.commit()
    def update_item(self,asin):
        name = session.query(User).filter_by(name=self.username).one()
        item = eval(name.item)
        print type(name.item)
        if asin in item:
            item[asin] = item[asin]+1
        else:
            item[asin] = 1
        name.item = json.dumps(item)
        print name.item
        session.add(name)
        session.commit()
    def delete_item(self,asin):
        name = session.query(User).filter_by(name=self.username).one()
        item = eval(name.item)
        if asin in item:
            item[asin] = item[asin]-1
            if item[asin]==0:
                del item[asin]
        name.item = json.dumps(item)
        session.add(name)
        session.commit()
    def buy(self):
        name = session.query(User).filter_by(name=self.username).one()
        name.item = "{}"
        session.add(name)
        session.commit()
'''
update = DBupdate("liuhpleon")
update.delete_item("B00F5UD4MG")            
'''            
