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
print('the following command will be run and its output logged:\n%s\n' % command)
with Popen(command, shell=True, stdout=PIPE, bufsize=1) as sp:
    for line in sp.stdout:
        #print('%d sec: ' % (time() - now), end='', flush=True)
        #print(logging.info(line))
        #print('\n', end='', flush=True)
        with open('download.txt', 'a') as filehandle:	
          filehandle.write('%s\n' % str(line, 'utf-8'))  
