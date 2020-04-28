#!/usr/bin/python3
import json
import subprocess

f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   print(url)
   try:     
    command = "sudo curl -L '" + url + "' -o " + news + ".xml"
    subprocess.call(command, shell=True)
    
    print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)

command = "sudo python3 updateDate.py"
subprocess.call(command, shell=True)
command = "sudo ./gitupdater.sh"
subprocess.call(command, shell=True)
#!/usr/bin/python3
import json
import subprocess

f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   print(url)
   try:     
    command = "sudo curl -L '" + url + "' -o " + news + ".xml"
    subprocess.call(command, shell=True)
    
    print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)

command = "sudo python3 updateDate.py"
subprocess.call(command, shell=True)
command = "sudo ./gitupdater.sh"
subprocess.call(command, shell=True)

