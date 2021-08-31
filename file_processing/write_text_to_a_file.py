# create a new file with the path to the location you want it to be, add "w" as the second param to the open function
with open("veggies.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")

# read the bear.txt file and print out the first 90 characters of its content
with open("bear.txt") as myfile:
    content = myfile.read()

print(content[:90])


# Define a function that gets a single string "character" and a "filepath" as params and returns the number of occurences of that character in the file

def foo(character, filepath = "bear.txt"):
    with open(filepath) as myfile:
        content = myfile.read()
    return content.count(character)

#ALTERNATE
def foo(character, filepath = "bear.txt"):
    file = open(filepath)
    content = file.read()
    file.close()
    return content.count(character)

print(foo('a', 'bear.txt')) # returns 39