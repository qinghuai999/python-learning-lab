"""
Task

Write a program that takes the average of an arbitrary number of floats. The number of floats and the floats themselves are all entered by the user

Do this in the following way:

Prompt the user to enter the number of floats to be entered. (This is in the starter code already.)
Repeatedly prompt the user for those numbers using a while loop.
Accumate the numbers into a running total and then print the average of the numbers.
Preconditions

The number of floats entered is an integer greater than zero.
The subsequent floats are each greater than or equal to zero.
"""

"""
# Method One
number_of_floats = int(input('Please enter the number of int: '))
count = number_of_floats
total_number = 0
while count > 0:
    float_number = float(input('Enter a number: '))
    count = count - 1
    total_number += float_number

avgNumber = round(total_number / number_of_floats, 2)
print(avgNumber)
# </editor-fold>
"""

# Optimized Method
number_of_floats = int(input('Please enter the number of float: '))
total = 0
for _ in range(number_of_floats):
    number = float(input('Enter a number: '))
    total += number

average = total / number_of_floats
print(f"{average:.2f}")

