import subprocess
from datetime import date
from datetime import datetime
from updateDropbox import upload


def updateDate():
 now = datetime.now()
 date_string = now.strftime("%A, %B %d %Y %r")
 command = str(date_string) + " NZ"
 with open("lastNewsUpdate.txt", "wb") as f:
  f.write(command.encode('utf-8'))
  f.close()
  upload("lastNewsUpdate.txt")
