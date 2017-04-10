'''
Created on Feb 27, 2017

@author: haopeng
'''
from cassandra.cluster import Cluster
import json
cluster = Cluster(port=9043)
session = cluster.connect()
def insert_data(asin,title,price,image,description,category):
    try:
        session.execute(
        """
        INSERT INTO iteminfo.test (asin, title, price,image,description,category)
        VALUES (%s, %s, %s,%s,%s,%s)""",
        (asin,title,price,image,description,category))
    except:
        print "insert error" 
        return False
    return True    
    
file = open("/home/haopeng/Data/MovieTV_for_save.json","r+")
line = file.readline()
asin = None
title = None
price = None
image = None
category = None
description = None

while(line!=None):
    set = eval(line)
    try:
        asin = set["asin"]
    except:
        asin = ""
    try:
        title = set["title"]
    except:
        title = ""
    try:
        price = set["price"]
    except:
        price = -1
    try:
        image = set["image"]
    except:
        image = ""
    try:
        description = set["description"]
    except:
        description = ""
    try:
        category = set["category"]
    except:
        category = ""
    
    insert_data(asin, title, price, image, description,category)
    line = file.readline()