"""
Task

Write a program that uses a while loop to repeatedly prompt the user for numbers until the user enters nothing (empty string). Print the average of the numbers entered.

You must use a break statement to exit the while loop in order to credit for this question.
"""
# By myself
total = 0.0
count = 0.0
while True:
    number = input('Enter a number: ')
    if number == '':
        break
    number = float(number)
    total += number
    count += 1

average = total / count
print(f"{average:.1f}")


