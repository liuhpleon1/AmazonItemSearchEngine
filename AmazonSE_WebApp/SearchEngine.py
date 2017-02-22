from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
from UserDBregister import DBregister
from UserDBsearch import DBsearch
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def login_SE():
    if request.method=='POST':
        data = request.form
        username = data.get('username').__str__()
        password = data.get('password').__str__()
        search_user = DBsearch(username,password)
        result = search_user.search_user()
        login_info = {'username':result[0],'password':result[1]}
        print result
        print login_info
        return jsonify(login_info)
    else:
        return render_template("login.html")

@app.route('/signup/',methods = ['GET','POST'])
def signup_SE():
    if request.method =='POST':
        data = request.form
        print data
        username = data.get('username').__str__()
        password = data.get('password').__str__()
        email = data.get('email').__str__()
        cellphone = data.get('cellphone').__str__()
        register = DBregister(username,password,email,cellphone)
        check = register.register_user()
        return jsonify({"username":check[0],'email':check[1],'cellphone':check[2]})
    else:
        return render_template("signup.html")
    
    
@app.route('/forget/',methods = ['GET','POST'])
def forget_SE():
    return render_template('forget.html')


@app.route('/search/',methods = ['GET','POST'])
def search_SE():
    if request=='POST':
        print "good"
    else:
        return render_template('search.html')







if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
    