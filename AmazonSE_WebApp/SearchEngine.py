from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
from UserDBsearch import DBsearch
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def login():
    if request.method=='POST':
        data = request.form
        username = data.get('username').__str__()
        password = data.get('password').__str__()
        result = False
        search = DBsearch(username,password)
        if search.search_user():
            result = True;
        print result
        return jsonify({"check":True})
    else:
        return render_template('login.html')
    
@app.route('/signup/',methods = ['GET','POST'])
def signup():
    return render_template("signup.html")
    
    
@app.route('/forget/',methods = ['GET','POST'])
def forget():
    return render_template('forget.html')


@app.route('/search/',methods = ['GET','POST'])
def search():
    return render_template('search.html')







if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
    