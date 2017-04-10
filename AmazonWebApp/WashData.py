import json 
import sys
path = "/home/haopeng/Data/"
name = "1.5m"
file = open(path+name+".json",'r+')
file0 = open(path+name+'_for_index.json', 'w')
#file1 = open(path+name+'_for_save.json', 'w')
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
        if title!="" :
            a0 = {"asin":asin,"title":title}  
            #a1 = {"asin":asin, "title":title, "price":price, "image":image, "description":description, "category":"clothes"}
            s0 = json.dumps(a0)
            #s1 = json.dumps(a1)
            file0.write(s0+"\n")
            #file1.write(s1+"\n")
    except:
        sys.exc_info()[0]
        print "read error----------------------" 
    i = i+1
    if i%10000==0:
        print i 
    item = file.readline()
    