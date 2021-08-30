# while loops
# runs as long as a condition is true

a = 10
while a > 0:
    print(a)
    a -= 1

user_name = ''
while user_name != 'Mason':
    user_name = input("Please enter a username: ")

# break and continue
user_name = ''
while True:
    user_name = input("Please enter a username: ")
    if user_name == 'Mason':
        break
    else:
        continue