import json
import subprocess
import requests
import re

def getYoutubeXML(link):
	x = requests.get(link)
	string = x.text
	match = re.findall(r"channelId\\\":\\\"[a-zA-Z0-9]*\\\"", string)
	split = match[1].split(":")
	id = split[1].replace("\"","")
	id = id.replace("\\", "")
	url = "https://www.youtube.com/feeds/videos.xml?channel_id="+id
	print(url)
	return url
	
news = input("keyword: " )
rss = input("xml: " )
title = input("title: " )

if "youtube" in rss:
	rss = getYoutubeXML(rss)
else:
    print("not a youtube link")
f = open('news.json')
json_string = f.read()
data = json.loads(json_string)
data[news] = rss
print(data)

with open('news.json', 'w') as outfile:
    json.dump(data, outfile)

f = open('newstitles.json')
json_string = f.read()
data = json.loads(json_string)
data[news] = title
print(data)

with open('newstitles.json', 'w') as outfile:
    json.dump(data, outfile)

subprocess.call("python3 updateNews.py", shell=True)
