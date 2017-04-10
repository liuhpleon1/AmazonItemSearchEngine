'''
Created on Mar 13, 2017

@author: haopeng
'''
from cassandra.cluster import Cluster
from cassandra.query import tuple_factory
import json
from pymongo.message import query

'''
explain ranking 

the tf-idf algorithm is used here

tf = count(word w in document d)/total(numbers of word in document d)

idf = total document/document contains (word a)

tf is easy

idf count be found = total document/ array(length)

we will use tf idf in title and description

and combine them

title weight is 0.8 and description weight is 0.2
(I personally mark this)

'''
''' this is the total number of our document'''
totaldoc = 940850

import math
def tf_idf(query,doc,asins):
    '''
    arraylen is how many document contains words(used in idf)
    doclen is how many word in doc(used in tf)
    wordtime is how manytimes word appear(used in tf)
    940850 is our total number of document (used in idf)
    '''
    arraylen = len(asins)
    doclen = len(doc.split())
    wordtime = count(query,doc)
    if doclen == 0:
        doclen = doclen+1
    if arraylen == 0:
        arraylen = arraylen+1
    tf = float(wordtime)/float(doclen)
    idf = math.log(940850/float(arraylen))
    return tf*idf
'''
count word number in title/description
'''
def count(query,document):
    appearsum = 0
    for word in query.split():
        '''
        print word
        print document
        '''
        appearsum = document.count(word)+appearsum
    return appearsum

cluster = Cluster(port=9043)
session = cluster.connect()
session.row_faoctory = tuple_factory
class Cassandra_search_title():
    def __init__(self,word):
        self.word = word
    def search(self): 
        row = session.execute("SELECT asin FROM itemtitleindex.test where word = '"+self.word+"'")
        try:
            asin = set(eval(row[0][0].__str__()))
            return asin
        except:
            return set()
        #print type(asin)
        #print len(asin)
        #print asin

class Cassandra_search_description():
    def __init__(self,word):
        self.word = word
    def search(self):
        row = session.execute("SELECT asin FROM itemdescindex.test where word = '"+self.word+"'")
        try:
            asin = set(eval(row[0][0].__str__()))
            return asin
        except:
            return set()
    
class Search_items():
    def __init__(self,word):
        wordlist = word.split()
        self.wordlist = wordlist
    def search(self):
        title = set()
        description = set()
        result = set()
        for word in self.wordlist:
            cur =  Cassandra_search_title(word).search()
            if len(title) == 0:
                title = title | cur
            else:
                title = title & cur
        
        for word in self.wordlist:
            cur = Cassandra_search_description(word).search()
            if len(description) == 0:
                description = description | cur
            else:
                description = description & cur
        result = title | description
        print len(result)
        return result
    
class Get_info:
    def __init__(self,asin):
        self.asin = asin
    
    def user_get(self):
        try:
            row = session.execute("SELECT title,description,price,image,category,asin FROM iteminfo.test where asin = '"+self.asin+"'"+" limit 1000") 
            item = {"title":row[0][0],"description":row[0][1],"price":row[0][2],"imgurl":row[0][3],"category":row[0][4],"asin":row[0][5]}
            return item
        except:
            return None
    
    def get(self,startprice,endprice,item_category):
        try:
            row = session.execute("SELECT title,description,price,image,category,asin FROM iteminfo.test where asin = '"+self.asin+"'"+" limit 1000")
            price = row[0][2]
            category = row[0][4]
            item = {"title":row[0][0],"description":row[0][1],"price":row[0][2],"imgurl":row[0][3],"category":row[0][4],"asin":row[0][5]}
            # test category
            if item_category!=None and category!=item_category:
                return None
            if price<startprice or  price>endprice:
                return None
            else:
                return item
        except:
            return None 
class Get_item:
    def __init__(self,query,startprice,endprice,category):
        self.query = query
        self.sp = startprice
        self.ep = endprice
        self.category = category
    def getinfo(self):
        s1 = Search_items(self.query)
        asins = s1.search()
        info = {}
        for asin in asins:
            item = Get_info(asin.__str__()).get(self.sp,self.ep,self.category)
            if item!= None:
                '''
                    score the data
                    first is the times that words appeals in document
                    second is the document length
                    third is the document number that contains word
                '''
                '''
                   covert all to lowercase in order to tf idf finding matches
                '''
                title_score = tf_idf(self.query.lower(),item["title"].lower(),asins)
                description_score = tf_idf(self.query.lower(),item["description"].lower(),asins)
                '''
                test for each scoring in tf-idf
                
                '''
                '''
                print self.query
                print item["title"]
                print item["description"]
                print title_score
                print description_score
                print "-----"
                '''
                
                score = title_score*0.8+description_score*0.2
                info[score]=item
        '''
        rank the item by score
        '''
        reversed(sorted(info))
        res = []
        '''
        test for info size
        '''
        #print len(info)
        '''
           return at most 400 result
        '''
        for key in info.keys():
            res.append(info.get(key))
            '''
            test to see if the ranking is from high to low
            '''
            '''
            print info
            print "\n"
            if(len(res)>3):
                break 
            '''
        return res

'''
test case
'''
'''
test count word 
print count("a","a a a a a a a a a")
'''
'''
test the whole program especially ranking
'''
'''
info = Get_item("dell",1,100000,None)
print info.getinfo()
'''
