# pass a file path to the open() function, store it in a varialbe to create a file object
myfile = open("fruits.txt")

#call the read() method on the file object and print it out to view its contents
print(myfile.read())

# Closing a File
myfile.close()




#ALTERNATE METHOD to read and close a file
# the close() method is not necessary here because the "with" context manager will apply the clost() method implicitly. It is generally better practice to use the with/as pattern

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)

with open("../alternate.txt") as myfile:
    file_content = myfile.read()

print(file_content)
