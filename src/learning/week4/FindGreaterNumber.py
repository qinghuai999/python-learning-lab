"""
File: FindGreaterNumber.py
Author: Shiqi Su
Date: 2025-08-22 11:57
Description: Check if a list has an element greater than a given one.
"""


def has_gt(xs: list[int], y: int) -> bool:
    """
    Check if a list has an element greater than a given one.

    This function goes through the list 'xs' and check if there is any element
    that is strictly greater than the number 'y'. It returns true if at least
    one element satisfies this condition, and False otherwise.

    Args:
        xs (list[int]): A list of integers to check
        y (int): The integer to compare against

    Returns:
        bool: True if there is an element in 'xs' greater than y,
        else return false.
    """
    for i in xs:
        if y < i:
            return True
    return False

print(has_gt([1,2,3], 2))