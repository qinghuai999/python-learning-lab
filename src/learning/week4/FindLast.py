"""
File: FindLast.py
Author: Shiqi Su
Date: 2025-08-22 11:54
Description: Find the index of the last occurrence of a given character in a string.
"""


def find_last(char: str, string: str) -> int:
    """
    Args:
        char (str): The character to search for.
        string (str): The whole string to search within.

    Returns:
        int: The index of the last occurrence of the character if found, otherwise -1.

    """
    word = -1
    for i, x in enumerate(string):
        if char == x:
            word = i
    return word


print(find_last("b", "baba"))
