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

command = "git add ."
subprocess.call(command, shell=True)
command = "git commit -m updated xml files"
subprocess.call(command, shell=True)
command = "git push --all"
subprocess.call(command, shell=True)
   