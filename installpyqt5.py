import subprocess

command = "pip install PyQt5-5.15.4-cp36.cp37.cp38.cp39-none-win_amd64.whl"

subprocess.call(command, shell=True)

command = "pip install PyGetWindow"

subprocess.call(command, shell=True)

command = "pip install pywin32"

subprocess.call(command, shell=True)

command = "pip install regex"

subprocess.call(command, shell=True)

command = "pip install requests"

subprocess.call(command, shell=True)

command = "pip install dropbox"

subprocess.call(command, shell=True)