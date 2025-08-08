"""
File: PowersOfTwo.py
Author: Shiqi Su
Date: 2025-08-08 20:33
Description: Write a program that takes a positive integer as an input. Output a simple table that lists the
powers of two up to the integer value passed to the program.
"""
number = int(input('Enter the power: '))
total_times = number
operation_count = 0

while 0 <= total_times:
    value = 2 ** operation_count
    print(operation_count, value)

    operation_count += 1
    total_times -= 1



