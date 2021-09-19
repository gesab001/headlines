#!/usr/bin/python3
import json
import subprocess
from updateDropbox import upload
import platform 
from datetime import date
from datetime import datetime


def updateDate():
 now = datetime.now()

 #print("now =", now)

 # dd/mm/YY H:M:S
 #time_string = now.strftime("%H:%M:%S")
 #print("date and time =", dt_string)	
 date_string = now.strftime("%A, %B %d %Y %r")
 command = "echo " + str(date_string) + " NZ" + " >lastNewsUpdate.txt"
 subprocess.call(command, shell=True)
 upload("lastNewsUpdate.txt")

command = "sudo git pull"
if platform.system()=="Windows":
  command = "gitpull"
subprocess.call(command,shell=True)
f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   filepath = news + ".xml"
   print(url)
   try:     
    command = "sudo curl -L '" + url + "' -o " + filepath
    if platform.system()=="Windows":
      command = "curl -L " + url + " -o " + filepath
    subprocess.call(command, shell=True) 
    print(filepath + " saved successfully" )
    upload(filepath)   
   except Exception as ex:
    print(ex)

updateDate()
command = "./deploy.sh"
if platform.system()=="Windows":
  command = "deploy"
subprocess.call(command, shell=True)
