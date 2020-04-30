#!/usr/bin/python3
import cgitb
import cgi
import subprocess
import json

#import mysql.connector as conn
cgitb.enable()  
#form = cgi.FieldStorage()
  
#news = form.getvalue('keyword')
#rss = form.getvalue('url')
#title = form.getvalue('title')

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")

f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   #print(url)
   try:     
    command = "curl -L '" + url + "' -o " + news + ".xml"
    
    print(subprocess.call(command, shell=True))
    
    #print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)

command = "sudo python3 updateDate.py"
subprocess.call(command, shell=True)
command = "sudo ./gitupdater.sh"
subprocess.call(command, shell=True)

#print("finished updating news")
