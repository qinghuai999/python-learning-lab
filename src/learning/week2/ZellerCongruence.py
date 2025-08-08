"""
Research Zeller's congruence, and write a program which takes as input,
the day of the month, the month, and the year, and prints the day of the week corresponding to that date. Design a
set of example cases to check you've implemented the logic correctly.
"""

any_day = int(input('Enter day: '))
any_month = int(input('Enter month: '))
any_year = int(input('Enter year: '))
# Zeller's formaula adjustment for Jan and Feb
if any_month == 1 or any_month == 2:
    any_month += 12
    any_year -= 1
q = any_day
m = any_month
k = any_year % 100
j = any_year // 100
zeller_formate = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(f"The day is: {days[zeller_formate]}")


