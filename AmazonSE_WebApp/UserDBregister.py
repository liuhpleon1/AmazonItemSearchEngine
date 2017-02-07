from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()
def register(input_name,input_password,input_email,input_phone,input_level):
    try:
        check = session.query(User).filter_by(name=input_name).one()
    except:
        newuser = User(name=input_name,password=input_password,email = input_email,phone=input_phone,level=input_level)
        session.add(newuser)
        session.commit()
        return True
    return False

register('haopeng','19921005','liupleon@gmail.com','9796767182',4)
