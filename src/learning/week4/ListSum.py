"""
File: ListSum.py
Author: Shiqi Su
Date: 2025-08-22 14:13
Description: Calculate the sum of all elements in a list of integers using a for loop.
"""
def sum_elems(xs: list[int]) -> int:
    """
    Calculate the sum of all elements in a list of integers using a for loop.


    This function iterates through each element of the input list and
    accumulates the total sum. It does not use the built-in 'sum' function.

    Args:
        xs (list[int]): A list of integers.

    Returns:
        int: The sum of all integers in the list.

    """
    total = 0
    for i in xs:
        total += i
    return total

print(sum_elems([1, 2, 3]))
