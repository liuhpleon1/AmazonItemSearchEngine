'''
Created on Feb 5, 2017

@author: Jessie
'''

import os
import json
from download import download
from time import sleep
ua = 'Chrome/56.0.2924.87'
class start: 
    def __init__(self,name):
        self.name = name
    def loop(self):
        file = open('Seed/'+self.name+".json","r+")
        print(file)
        data = json.load(file)
        for i in range(1,401):
            key = str(i)
            link = (data[key])[0]
            checked = (data[key])[1]
            print link 
            print checked
            d = download(ua,link,self.name+"_"+str(i),self.name)
            sleep(1)
            d.getpage()
            checked = False
            data[i] = [link,checked]
        #json.dump(data,file)
          
s = start("camera")
s.loop()
        
        
        