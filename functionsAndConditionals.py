# to create a function in python, use the "def" keyword
def mean(myList):
    the_mean = sum(myList) / len(myList)
    return the_mean

print(mean([1, 2, 3, 4, 5, 6, 7]))

# write a function that returns a number squared
def square_this_num(num):
    return num * num

# Conditionals
student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}

def average(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean
#ALTERNATE
def average(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

# Write a function that accepts a string and returns true if the length of the string is greater than or equare to 8, otherwise return false
def foo(string):
    if len(string) >= 8:
        return True
    else:
        return False