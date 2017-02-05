'''
Created on Feb 5, 2017

@author: Jessie
'''

import os
class dir:
    def __init__(self,name):
        self.name = name
        
    def make(self):
        os.mkdir("E:/CS179GData/"+self.name+"/")
            
for i in os.listdir('Seed'):     
    s = dir(str(i)[0:len(str(i))-4]);
    s.make()
        
        
        