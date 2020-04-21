import json
import subprocess

f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   print(url)
   try:
    command = "curl '" + url + "' -o " + news + ".xml"
    subprocess.call(command, shell=True)
   
    print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)

command = "./gitupdater.sh"
subprocess.call(command, shell=True)
