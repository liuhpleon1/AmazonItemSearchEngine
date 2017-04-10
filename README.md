How to use the my code:

Haopeng Liu ;)


1. What you need to have before running my Fake Amazon :)

-Python 2.7
  -Flask
  -Sqlachemy
  -Python Cassandra driver

running command in terminal:
ssh -L 9161:spark17.cs.ucr.edu:9160 -L 9043:spark18.cs.ucr.edu:9042 hliu@bolt.cs.ucr.edu

put it into a proper position or change my path.



2. Check my cassandra in bolt cs edu:

ssh hliu@bolt.cs.ucr.edu

password: Lhp19921005

cs179g_login 1

cqlsh spark17

there are three tables in my cassandra:

select * from iteminfo.test;  for check my item

select * from itemtitleindex.test; for check my title

select * from itemdescindex.test;  for check my description


3. How you can taset my code

   for the search engine.py you just simply run it. this is the core part for search engine

   for cassandra_search.py  this is the cassandra search and ranking part, I have created a lot of test case and comment for this part and notes them, please feel free to use it.

   for the userinfo...py parts, they are how I build, search and and update the user database, this is write by sqlachemy, so does the cache part, this will show a rank of count what people
   often search.

   The other part is not used in web backend, just ignore them.

4. for front end:

   all front end document stored in template(for html) and static (js and css)
   
   jinja2 is used inside flask framework so we have to store our front end like this

   for front end part, each html document related with one js file and css file are responsible for all html.


5. Please contact me via phone: 979 676 7182 or email hliu033@ucr.edu

   if you need any assistance


  


