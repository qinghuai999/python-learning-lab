"""
File: LeapYear.py
Author: Shiqi Su
Date: 2025-08-08 20:36
Description: A leap year occurs when the year is a multiple of four, unless the year is a multiple of 100.
However, if the year is a multiple of 400, then it is a leap year. For instance, 2016 and 2000
are leap years, but 1900 is not.
Create a new Python source file, and write a program leap_year.py which asks the user to
enter an integer (representing a year), and prints True if the year is a leap year, and False if
not.
"""
for _ in range(5):
    yearNumber = int(input('Please enter a year: '))
    if (yearNumber % 4 == 0 and yearNumber % 100 != 0) or (yearNumber % 400 == 0):
        print(True)
    else:
        print(False)
