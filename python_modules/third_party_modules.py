import time
import os
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv") # type(data) = <class 'pandas.core.frame.DataFrame'>
        print(data.mean())
    else:
        print("file does not exists")
    time.sleep(4)

#install pandas with pip3.9
