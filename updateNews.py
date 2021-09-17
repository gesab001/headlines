#!/usr/bin/python3
import json
import subprocess
import platform

command = "sudo git pull"
if platform.system()=="Windows":
  command = "gitpull"
subprocess.call(command,shell=True)
f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   print(url)
   try:     
    command = "sudo curl -L '" + url + "' -o " + news + ".xml"
    if platform.system()=="Windows":
      command = "curl -L " + url + " -o " + news + ".xml"

    subprocess.call(command, shell=True)
    
    print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)

command = "python3 updateDate.py"
subprocess.call(command, shell=True)

command = "./deploy.sh"
if platform.system()=="Windows":
  command = "deploy"
subprocess.call(command, shell=True)
