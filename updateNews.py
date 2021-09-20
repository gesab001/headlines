#!/usr/bin/python3
import json
import subprocess
from updateDropbox import upload
import platform 
from datetime import date
import datetime

import sys
import requests
import time
   
def updateDate():
 now = datetime.datetime.now()
 date_string = now.strftime("%A, %B %d %Y %r")
 command = str(date_string) + " NZ"
 with open("lastNewsUpdate.txt", "wb") as f:
  f.write(command.encode('utf-8'))
  f.close()
  upload("lastNewsUpdate.txt")

def updateAuto(interval):
    while True:
        print("updating news")
        getAllCurrentNews()
        print("update successful")
        now = datetime.datetime.now()
        added_seconds = datetime.timedelta(0,interval)
        new_datetime = now + added_seconds
        nextUpdate = new_datetime.strftime("%A, %B %d %Y %r")
        print("next update is " + nextUpdate)
        time.sleep(interval)
        
        
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
 if option=="--auto":
   interval = int(sys.argv[2]) * 60
   updateAuto(interval)