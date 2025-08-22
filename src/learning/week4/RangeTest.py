"""
File: RangeTest.py
Author: Shiqi Su
Date: 2025-08-22 14:44
Description: Understanding how to use range class.
"""


def sum_range(start: int, end: int) -> int:
    """
    Calculate the sum of numbers in a given range.

    This function uses Python's built-in 'range' to compute
    the sum of all integers starting from 'start' up to,
    but not including, 'end'.

    Args:
        start (int): the starting integer.
        end (int): the ending integer.

    Returns:
        int: The sum of all integers from 'start' to 'end' - 1.

    """
    arr = range(start, end)
    sum = 0
    for i in arr:
        sum += i
    return sum


print(sum_range(0, 5))


def sum_evens(start: int, end: int) -> int:
    """
    Calculate the sum of even numbers in a given range.

    This function uses Python's built-in 'range' to compute
     the sum of all even integers starting from 'start' up to,
     but not including, 'end'.
    Args:
        start (int): the starting integer.
        end (int): the ending integer.

    Returns:
        int: The sum of all even integers from `start` to `end - 1`.
    """
    if start != 0 and start % 2 != 0:
        start += 1
    arr = range(start, end, 2)
    count = 0
    for i in arr:
        count += i
    return count


print(sum_evens(3, 5))
