from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
from UserDBregister import DBregister
from UserDBsearch import DBsearch
from CacheDBsetup import Cache
from CacheDBupdate import Update

engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

if_login_username=''

@app.route('/',methods = ['GET','POST'])
def login_SE():
    if request.method=='POST':
        data = request.form
        username = data.get('username').__str__()
        password = data.get('password').__str__()
        search_user = DBsearch(username,password)
        result = search_user.check_user()
        login_info = {'username':result[0],'password':result[1]}
        if_login_username = result[0]
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
    if request.method =="POST":
        data = request.form
        username = data.get("username").__str__()
        email = data.get("email").__str__()
        cellphone = data.get("cellphone").__str__()
        print username
        print email
        print cellphone
        if username!=None:
            search_by_username = DBsearch(username,None)
            password = search_by_username.search_user()
            return jsonify({"password":password})
        else:
            if email!=None:
                search_by_email = DBsearch(None,None)
                info = search_by_email.search_email(email)
                return jsonify({"username":info[0],"password":info[1]})
            else:
                search_by_phone = DBsearch(None,None)
                info = search_by_phone.search_cellphone(cellphone)
                return jsonify({"username":info[0],"password":info[1]})
    else:
        return render_template('forget.html')


@app.route('/search/',methods = ['GET','POST'])
def search_SE():
    if request.method=='POST':
        data = request.form
        query = data.get("query").__str__()
        if query!= None:
            new_recent_query = Update(query)
            new_recent_query.add()
            info = new_recent_query.forward()
            res = []
            for key in info:
                res.append(key[0])
                if len(res)==15:
                    break
            print res
            return jsonify({"rank":res})
    else:
        return render_template('search.html')







if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
    