# User Input

def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Colde"

# to get a value from the use, use the input function
user_input = input("Enter temperature:")

print(type(user_input)) # returns <class 'str'>

user_input = float(user_input) #convert str to float, could also use int but int will only work with whole numbers while floats can accomodate a decimal point

print(type(user_input)) #returns <class 'float'>

print(weather_condition(user_input))