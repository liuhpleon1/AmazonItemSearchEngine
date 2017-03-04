import json 
import sys
from flask import jsonify
file = open('E:/Movies_and_TV.json','r+')
file0 = open('E:/Movies_and_TV_for_index.json', 'w')
file1 = open('E:/Movies_and_TV_for_save.json', 'w')
i = 0;
item = file.readline()
while(item!=None):
    item_data = item.__str__()
    items = eval(item_data)
    asin = ""
    title = ""
    category = ""
    price = -1
    image = ""
    description = ""
    try:
        try:
            asin = items["asin"].__str__()
        except:
            asin = ""
        try:
            title = items["title"].__str__()
        except:
            title = ""
        try:
            price = items["price"]
        except:
            price = -1
        try:
            image =  items["imUrl"].__str__()
        except:
            image = ""
        try:
            description = items["description"].__str__()
        except:
            description = ""
        if title!=None :
            #a0 = {"asin":asin,"title":title}  
            a1 = {"asin":asin, "title":title, "price":price, "image":image, "description":description, "category":"Movies_and_TV"}
            #s0 = json.dumps(a0)
            s1 = json.dumps(a1)
            #file0.write(s0+"\n")
            file1.write(s1+"\n")
    except:
        sys.exc_info()[0]
        print "read error----------------------" 
    i = i+1
    item = file.readline()