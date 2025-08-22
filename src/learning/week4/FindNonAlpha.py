"""
File: FindNonAlpha.py
Author: Shiqi Su
Date: 2025-08-22 11:55
Description: Find a tuple of the indices of all the non-alphabetic characters in string
"""


def find_non_alpha(string: str) -> tuple[int]:
    """
    Find a tuple of the indices of all the non-alphabetic characters in string
    Args:
        string (str): A whole string to search within.

    Returns:
        tuple[int]: The index of the character if found.

    """
    arr = ()
    for i, ch in enumerate(string):
        # if ch.isdigit():
        if '0' <= ch <= '9':
            arr += i,
    return arr


print(find_non_alpha('ab1c2'))
