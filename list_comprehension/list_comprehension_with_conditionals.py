temps = [ 221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

# or

new_temps = [temp / 10 for temp in temps if temp > 0]

print(new_temps)


# Return only integers from the list of integers and strings
demo_list = [12, 2334, 2345, 322, 'Hello', 'World', 234, 'Dog', 555, 'Cat']
def return_only_integers(arr):
    new_list = [item for item in arr if isinstance(item, int)]
    return new_list

print(return_only_integers(demo_list))


# return only positive numbers from the list
demo_numbers = [ -3, -6, -7, 100, 123, -6, -5, 777, 888, 444, 0, -2, 982374]
def only_positives(numbers):
    return [num for num in numbers if num > 0]

print(only_positives(demo_numbers))

# List Comprehension with If/Else conditionals
# you need to put the for-in loop after the defintion of the conditional
temps = [ 221, 234, 340, -9999, 230]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

# return the same list but with zeros instead of strings
demo_list = [12, 2334, 2345, 322, 'Hello', 'World', 234, 'Dog', 555, 'Cat']
def zeros_only(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

# Define a function that takes a list as a param that contains decimal numbers as strings and returns the sum of those numbers. For example, if the input was ['1.2', '2.6', '3.3'], it should return 7.1.
def convert_and_sum(arr):
    answer = sum(float(i) for i in arr)
    return answer