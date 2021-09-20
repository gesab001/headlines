import requests
import json

f = open("news.json")
json_string = f.read()
rss = json.loads(json_string)

url = rss["nzherald"]
print(url)
res = requests.get(url)
xmlString = res.text
print(xmlString)
file_path = "nzherald.xml"
with open(file_path, "wb") as f:
  f.write(xmlString.encode('utf-8'))