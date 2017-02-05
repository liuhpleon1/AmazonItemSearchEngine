import urllib2

class download():
    def __init__(self,user_agent,url,name,filename):
        self.user_agent = user_agent
        self.url = url
        self.name = name
        self.filename = filename
        
    def getpage(self):  
        headers = { 'User-Agent' : self.user_agent } 
        request = urllib2.Request(self.url,"",headers)
        respone = urllib2.urlopen(request)
        f = open("E:/CS179GData/"+self.filename+"/"+self.name+".html",'w');
        f.write(respone.read())  
            
#d = download('Chrome/56.0.2924.87',"https://www.amazon.com/s/ref=nb_sb_noss_2?url=node%3D565098&field-keywords=desktop","a") 
#d.getpage()   