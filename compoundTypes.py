# List
# you can store multiple objects in a list

student_grades = [9.1, 8.8, 7.5]

# using "range", you can create a list of numbers automatically
# the first two arguments are the range (inclusive of the first and noninclusive of the last), a third parameter can be provided and it is the step.
example_list = list(range(1, 10))
second_list = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]
print(example_list)

# Attributes
dir(list) # will print all the methods and attributes you can do on a list. Also works for any datatype

dir(__builtins__) # displays all built in functions

sum_of_grades = sum(student_grades)
count_of_grades = len(student_grades)

average_of_grades = sum_of_grades / count_of_grades

print(average_of_grades)