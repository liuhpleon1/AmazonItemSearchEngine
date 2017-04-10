import json
name = "item_1m"
file_read = open("/home/haopeng/UCR-Courses/CS236/Project/Data/"+name+".json","r+")
file_write = open("/home/haopeng/UCR-Courses/CS236/Project/Data/"+name+"_index.json","w")

line = file_read.readline()
while(line!=None):
    lineinfo = eval(line)
    asin = lineinfo["asin"]
    title = lineinfo["title"]
    line = {"asin":asin, "title":title}
    newinfo = json.dumps(line)
    file_write.write(newinfo+"\n")
    line = file_read.readline()