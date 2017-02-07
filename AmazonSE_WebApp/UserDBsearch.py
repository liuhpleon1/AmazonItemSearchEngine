from UserDBsetup import User,base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

def search(input_name,input_password):
    user = ""
    try:
        user = session.query(User).filter_by(name = input_name).one()
    except:
        return False
    if user == "": 
        return False
    elif user.password!=input_password:
        return False
    else:
        return True

print search('haopeng','19921005')