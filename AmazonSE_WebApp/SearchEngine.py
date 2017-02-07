from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def login():
    return render_template('login.html')
    
@app.route('/signup/',methods = ['GET','POST'])
def signup():
    if request.method=='POST':
        return redirect(url_for('log_in'))
    else:
        return render_template("signup.html")
    
@app.route('/forget/',methods = ['GET','POST'])
def forget():
    if request.method=='POST':
        return redirect(url_for(login))
    else:
        return render_template('forget.html')

@app.route('/search/',methods = ['GET','POST'])
def search():
    output = "<h1>search waiting</h1>"
    return output
@app.route('/result/',methods = ['GET','POST'])
def result():
    output = "<h1>result waiting</h1>"
    return output






if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
    