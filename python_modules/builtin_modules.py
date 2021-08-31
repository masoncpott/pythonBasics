#import modules at the top
import time

# dir(__builtins__) in python shell to view all built in functions and methods

# "import sys"
# "sys.builtin_module_names" to view a list of built in modules of the python software

# then import the module

# for example: import time
# dir(time) to view all functions/methods of the "time" module

while True:
    with open('../alternate.txt') as file:
        print(file.read())
        time.sleep(10)