'''
Created on Mar 1, 2017

@author: haopeng
'''
from cassandra.cluster import Cluster
import json
cluster = Cluster(port=9043)
session = cluster.connect()
def insert_data(word,asin):
    try:
        
        session.execute(
        """
        INSERT INTO itemtitleindex.test (word, asin)
        VALUES (%s, %s)""",
        (word,asin))
        
        '''
        session.execute(
        """
        INSERT INTO itemdescindex.test (word, asin)
        VALUES (%s, %s)""",
        (word,asin))
        '''
    except:
        print "insert error" 
        return False
    return True    
    
file = open("/home/haopeng/Data/inverted_index_title.json","r+")
line = file.readline()

word = None
asin = None

while(line!=None):
    set = eval(line)
    try:
        word = set["word"]
    except:
        asin = ""
    try:
        asin = set["asin"]
    except:
        asin = ""
    asin_str = asin.__str__()
    insert_data(word,asin_str)
    line = file.readline()