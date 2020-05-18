#!/usr/bin/python3
import json
import subprocess

f = open("/var/www/html/headlines/news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   print(url)
   try:     
    command = "sudo curl -L '" + url + "' -o /var/www/html/headlines/" + news + ".xml"
    subprocess.call(command, shell=True)
    
    print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)

command = "sudo python3 /var/www/html/headlines/updateDate.py"
subprocess.call(command, shell=True)
command = "sudo /var/www/html/headlines/gitupdater.py"
subprocess.call(command, shell=True)
