import json
import subprocess

news = input("keyword: " )
rss = input("xml: " )
title = input("title: " )
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
