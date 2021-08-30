# string formatting

user_input = input("enter your name: ") #get user input, store in a variable
message = "Hello %s!" % user_input #construct the message. the '%s' will be replaced by the variable variable after the '%' after the double quote
alternate_message = f"Hello {user_input}!"
print("Message:", message)
print("Alternate version: ", alternate_message)




# String Formatting with Multiple Variables
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
when = "today"

name_message = "Hello %s %s!" % (first_name, last_name)
alternate_name_message = f"Hello {first_name} {last_name}! What is up {when}?"

print("Name Message: ", name_message)
print("Alternate Name Message: ", alternate_name_message)