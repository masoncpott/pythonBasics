# python shell and terminal tips
# to clear the command line, execute: clear
# clear the python shell: cntrl + l
# to exit the shell back to the terminal: exit()

# Lists
# dir(list) to see what you can do with a list
# help(list.append)
monday_temps = [9.1, 8.8, 7.5]
monday_temps.append(8.1)
monday_temps.index(8.1) # returns 3

#apppend the value of "current" to the end of the list "seconds". use the list.append() method to do that.
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)

#Remove item 1.4534345567 from seconds
seconds.remove(1.4534345567)

# Accessing List Items
monday_temps.__getitem__(1)
# is equivalent to:
monday_temps[1]

# Complete the script so that it prints out the 3rd item of the list "serials":
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

# Append the first item of "weekend" to "workdays"
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])

# Accessing List Slices
monday_temps[1:4] #returns: [8.8, 7.5, 8.1]
# to return the last item in a list, use -1
monday_temps[-1] #returns: 8.1

# Print out the slice ['b', 'c', 'd'] from letters:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

# Print out the slice ['e', 'f', 'g'] from letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])

# Accessing Items in Dictionaries
student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}
student_grades["Sam"] # returns: 8.8