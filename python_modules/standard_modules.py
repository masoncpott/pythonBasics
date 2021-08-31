import time
import os

while True:
  if os.path.exists("../alternate.txt"):
      with open("../alternate.txt") as file:
          print(file.read())
  else:
      print("file does not exists")
  time.sleep(10)

# import os module
# sys.prefix
# dir(os)
# os.path.exists(filepath) --> returns a boolean

# to view all python modules, run this from the command line: open /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9
