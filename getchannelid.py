import requests
import subprocess
import re
import requests

	
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
	
url = input("youtube link: ")

if "youtube" in url:
	getYoutubeXML(url)
else:
    print("not a youtube link")
