import json

news = input("news: " )
rss = input("rss: " )
f = open('news.json')
json_string = f.read()
data = json.loads(json_string)
data[news] = rss
print(data)

with open('news.json', 'w') as outfile:
    json.dump(data, outfile)
