# for loops

#print each temp rounded to the nearest whole number
monday_temps = [9.1, 8.8, 7.6]
for temp in monday_temps:
    print(round(temp))

# print each letter in the word 'hello'
for letter in 'hello':
    print(letter)

#if color value is greater than 50, print out the value of that color
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color > 50:
        print(color)

#if color is of type integer, print it out
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int):
        print(color)