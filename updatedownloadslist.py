#!/usr/bin/env python3
import os
import cgitb
import cgi
import json

#import mysql.connector as conn
cgitb.enable()  
#form = cgi.FieldStorage()
 
#filename = form.getvalue('filename')
#url = form.getvalue('url')

#print ('Content-Type: application/json\n\n')

arr = os.listdir('./videos')

json_data = {}
json_data["downloaded"] = arr


with open ("downloadedvideos.json", "w") as outfile:
  json.dump(json_data, outfile)
# Do something with 'myjson' object


#print (json.dumps(json_data))  
