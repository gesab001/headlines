#!/usr/bin/env python3
import logging
from subprocess import PIPE, Popen
from time import time
import cgitb
import cgi

#import mysql.connector as conn
cgitb.enable()  
form = cgi.FieldStorage()
 
filename = form.getvalue('filename')
url = form.getvalue('url')

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
#news = input("news: " )
#rss = input("rss: " )
#print(filename)
#print(url)

now = time()
lines = []
command = "sudo youtube-dl -f mp4 " + url +  " -o ./videos/" + filename

with Popen(command, shell=True, stdout=PIPE, bufsize=1) as sp:
    for line in sp.stdout:
        lines.append(str(line, 'utf-8'))
    print("downloaded successful")
