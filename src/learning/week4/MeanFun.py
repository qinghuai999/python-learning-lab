"""
File: MeanFun.py
Author: Shiqi Su
Date: 2025-08-22 14:21
Description: Calculate the mean (average) value of a list of integers.
"""


def mean(xs: list[int]) -> float:
    """
    Calculate the mean (average) value of a list of integers.

    This function takes a list of integers, adds up all the elements,
    and divides the total by the number of elements.
    It returns the result as a float.

    Args:
        xs (list[int]): A list of integers.

    Returns:
        float: The mean (average) of the numbers in the list.

    """
    avg = 0
    count = 0
    for i in xs:
        count += i

    avg = count / len(xs)
    return round(avg, 1)


print(mean([2, 7, 3, 9, 13]))
