student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}

for grade in student_grades.items():
    print(grade)
    # prints out tuples for each pair of keys and values
    # ('Mary', 9.1)
    # ('Sam', 8.8)
    # ('John', 7.5)

for grade in student_grades.keys():
    print(grade)
    # prints out the keys
    # Mary
    # Sam
    # John

for grade in student_grades.values():
    print(grade)
    # prints out the values
    # 9.1
    # 8.8
    # 7.5

# make the code print out:
# John Smith: +37682929928
# Marry Simpons: +423998200919
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

#print out the numbers but replace the "+" sign with "00"
for value in phone_numbers.values():
    print(value.replace("+", "00"))