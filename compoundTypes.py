# List
# you can store multiple objects in a list

monday_temps = [9.1, 8.8, 7.5]

# using "range", you can create a list of numbers automatically
# the first two arguments are the range (inclusive of the first and noninclusive of the last), a third parameter can be provided and it is the step.
example_list = list(range(1, 10))
second_list = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]
print(example_list)

# Attributes
dir(list) # will print all the methods and attributes you can do on a list. Also works for any datatype

dir(__builtins__) # displays all built in functions

sum_of_temps = sum(monday_temps)
count_of_temps = len(monday_temps)

average_of_temps = sum_of_temps / count_of_temps

print(average_of_temps)

# Dictionary (key:value pairs, similar to a JS object)
# dir(dict)
# help(dict.values) etc

student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}
sumOfGrades = sum(student_grades.values())
print("sum of grades:", sumOfGrades)
countOfGrades = len(student_grades)
print("count of grades", countOfGrades)
avgGrades = sumOfGrades / countOfGrades
print("average of student grades:", avgGrades)