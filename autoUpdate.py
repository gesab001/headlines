from updateDropbox import upload
import platform 
from datetime import date
import datetime

import sys
import requests
import time
   
def updateAuto(interval):
    while True:
        print("updating news")

        print("update successful")
        now = datetime.datetime.now()
        added_seconds = datetime.timedelta(0,interval)
        new_datetime = now + added_seconds
        nextUpdate = new_datetime.strftime("%A, %B %d %Y %r")
        print("next update is " + nextUpdate)
        time.sleep(interval)
        
updateAuto(1)