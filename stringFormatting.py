# string formatting

user_input = input("enter your name: ") #get user input, store in a variable
message = "Hello %s!" % user_input #construct the message. the '%s' will be replaced by the variable variable after the '%' after the double quote
alternate_message = f"Hello {user_input}!"
print("Message:", message)
print("Alternate version: ", alternate_message)