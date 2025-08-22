"""
File: ListAllGreaterElement.py
Author: Shiqi Su
Date: 2025-08-22 12:27
Description: Return all elements in the list that are strictly greater than a given number
"""


def all_gt(xs: list[int], n: int) -> list[int]:
    """
    Return all elements in the list that are strictly greater than a given number

    This function iterates through the list of integers 'xs' and collects all
    numbers that are strictly larger than the integer 'n'. The result is returned
    as a new list. If no elements are greater than 'n', an empty list is returned.

    Args:
        xs (list[int]): A list of integer to check.
        n (int): The threshold number to compare against.

    Returns:
        list[int]: A list containing all integers from 'xs' that are strictly
        greater than 'n';

    """
    arr = []
    for i in xs:
        if i > n:
            arr.append(i)
    return arr


print(all_gt([1, 2, 3, 4], 2))
