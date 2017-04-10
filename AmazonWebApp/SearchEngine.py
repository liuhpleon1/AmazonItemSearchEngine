from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserDBsetup import User,base
from UserDBregister import DBregister, DBupdate
from UserDBsearch import DBsearch
from CacheDBsetup import Cache
from CacheDBupdate import Update
from Cassandra_search import Get_item, Get_info
engine = create_engine('sqlite:///user.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

myusername = ''

@app.route('/',methods = ['GET','POST'])
def login_SE():
    global myusername
    myusername = ''
    if request.method=='POST':
        data = request.form
        username = data.get('username').__str__()
        password = data.get('password').__str__()
        search_user = DBsearch(username,password)
        result = search_user.check_user()
        login_info = {'username':result[0],'password':result[1]}
        myusername = username
        print myusername
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
    global myusername
    print myusername
    if request.method=='POST':
        data = request.form
        #print data["query"]
        query = data.get("query").__str__()
        print query
        
        startprice = data.get("startprice").__str__()
        endprice = data.get("endprice").__str__()
        if startprice != "None" and startprice!="":
            startprice = int(startprice)
        else:
            startprice = -10
        if endprice != "None" and endprice!="":
            endprice = int(endprice)
        else:
            endprice = 1000000
            
        category = data.get("category").__str__()
        if category == "None":
            category = None
        print "category is "
        print category
        
        asin = data.get("asin").__str__()
        print asin
        if asin != "None":
            add = DBupdate(myusername)
            add.update_item(asin)
            return jsonify({"check":True})
        
        new_recent_query = Update(query)
        new_recent_query.add()
        info = new_recent_query.forward()
        res = []
        for key in info:
            res.append(key[0])
            if len(res)==15:
                break
        print res
        if query!="None":
            items = Get_item(query,startprice,endprice,category).getinfo()
            print len(items)
            return jsonify({"username":myusername,"rank":res,"item":items})
        else:
            return jsonify({"username":myusername,"rank":res,"item":None})
    else:
        return render_template('search.html')
 
    
@app.route('/info/',methods = ['GET','POST'])
def userinfo():
    global myusername
    if request.method=='POST':
        search = DBsearch(myusername,"")
        info = search.get_info()
        item = eval(info["item"])
        list = []
        for asin in item:
            item_info = Get_info(asin).user_get()
            amount = item[asin]
            title = item_info["title"]
            price = item_info["price"]
            category = item_info["category"]
            img = item_info["imgurl"]
            asin = item_info["asin"]
            item_have = {"title":title,"price":price,"category":category,"image":img,"amount":amount,"asin":asin}
            list.append(item_have)
        info["item"] = list
        print info
        data = request.form
        password = data.get("password").__str__()
        email =   data.get("email").__str__()
        cellphone = data.get("cellphone").__str__()
        asin = data.get("asin").__str__()
        buy = data.get("buy").__str__()
        print buy
        if buy == "true":
            print "into"
            update = DBupdate(myusername)
            update.buy()
            #return None
        if asin != "None":
            update = DBupdate(myusername)
            update.delete_item(asin) 
            #return None
        if password == "None" and email=="None" and cellphone=="None":
        #add = DBregister(myusername,c_password,c_email,c_cellphone)
            print "no update"
            return jsonify({"info":info})
        else:
            print "update"
            
            update = DBupdate(myusername)
            update.update_user(password, email, cellphone)
            search = DBsearch(myusername,"")
            info = search.get_info()
            
            return None
        
    else:
        return render_template("userinfo.html")
      




if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)