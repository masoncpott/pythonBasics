def area(x, y):
    return x * y

print(area(4, 5)) # returns 20

# write a function that takes two strings and concatenates them
def combine_strings(str1, str2):
    return str1 + str2

# DEFAULT and NON-DEFAULT params
def area(a = 4, b = 5):
    return a * b

# create a function that takes an unlimited number of arguments
def mean(*args):
    return sum(args) / len(args)

# define a function that takes an indefinite number of strings as params and returns a capitalized list of all the strings sorted alphabetically
def process_strings(*args):
    args = [item.upper() for item in args]
    return sorted(args)