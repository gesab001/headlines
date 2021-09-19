#!/usr/bin/python3
import json
import subprocess
import platform
import sys
import requests
import dropbox
import os



def upload(filename):
  token = "EeQL9hTvFSQAAAAAAAAAAaExBKMAKSKme_P--gT83PswjOO3azGirXzWPk14tYD_"
  dbx = dropbox.Dropbox(token)
  print("upload " + "/"+filename)
  #api = "{'path': 'filename.txt', 'mode': 'overwrite', 'autorename': 'false', 'mute': 'false', 'strict_conflict': 'false'}"
  #print(str(api))
  #parameters = {"Authorization": "Bearer " + token, "Dropbox-API-Arg": api, "Content-Type": "application/octet-stream" } 

  
  file_path = filename
  dest_path = os.path.join('/', filename)
  print ('Uploading %s to %s' % (file_path, dest_path))
  with open(file_path, 'rb') as f:
     values = f.read() 
     print(values)
     dbx.files_upload(values, dest_path, mute=True)
     #response=requests.post("https://content.dropboxapi.com/2/files/upload", headers=parameters, data=values)
     #print(response)



def download(filename):
  token = "EeQL9hTvFSQAAAAAAAAAAaExBKMAKSKme_P--gT83PswjOO3azGirXzWPk14tYD_"
  dbx = dropbox.Dropbox(token)
  print("download " + filename)
  with open("test.txt", "wb") as f:
    metadata, res = dbx.files_download(path="/stuffnz.xml")
    f.write(res.content)

if len(sys.argv)>1:
 option = sys.argv[1]
 if option=="--upload":
  filename = sys.argv[2]
  upload(filename)          
 if option=="--download":
  filename = sys.argv[2]
  download(filename)