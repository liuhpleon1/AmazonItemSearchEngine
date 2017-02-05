'''
Created on Feb 4, 2017

@author: Jessie
'''
import json
import os
class jsonify():
    def __init__(self,name):
        self.name = name; 
    def seed_transfer(self):
        try:
            data = {}
            file_read = open('E:/CS179GSeed/'+self.name,'r')
            jfile = open('Seed/'+self.name[0:len(self.name)-4]+'.json', 'w')
            for i in range(1,401):
                line = file_read.readline()
                data[i] = [line[0:len(line)-1],False]
                print str(i)+" "+line
            json.dump(data, jfile)
        except Exception as e:
            print e
            
for i in os.listdir('E:/CS179GSeed/'):
    j = jsonify(str(i));
    j.seed_transfer()
