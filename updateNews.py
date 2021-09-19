#!/usr/bin/python3
import json
import subprocess
from updateDropbox import upload
import platform 
from datetime import date
from datetime import datetime
import sys
import requests
    
def updateDate():
 now = datetime.now()
 date_string = now.strftime("%A, %B %d %Y %r")
 command = str(date_string) + " NZ"
 with open("lastNewsUpdate.txt", "w") as f:
  f.write(command)
  upload("lastNewsUpdate.txt")

def getAllCurrentNews():
    command = "sudo git pull"
    if platform.system()=="Windows":
      command = "gitpull"
    subprocess.call(command,shell=True)
    f = open("news.json")
    json_string = f.read()
    rss = json.loads(json_string)
    for news in rss:
      try:
       url= rss[news]
       file_path = news + ".xml"
       res = requests.get(url)
       xmlString = res.text
       print(xmlString)
       with open(file_path, "wb") as f:
        f.write(xmlString.encode('utf-8'))
      except:
        print("error on " + url)
    updateDate()
    command = "./deploy.sh"
    if platform.system()=="Windows":
      command = "deploy"
    subprocess.call(command, shell=True)

if len(sys.argv)>1:
 option = sys.argv[1]

else:
  getAllCurrentNews()
  