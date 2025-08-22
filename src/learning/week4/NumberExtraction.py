"""
File: NumberExtraction.py
Author: Shiqi Su
Date: 2025-08-22 22:23
Description:
"""


def get_number(string: str) -> int | None:
    """
    Extract the first positive integer from a given string.

    Args:
        string (str): Input string that may contain digits.

    Returns:
        int | None: The first integer found in the string,
        or None if no integer is present.

    """
    number = ''
    is_number = False
    for i in string:
        if i.isdigit() and int(i) > 0:
            number += i
            is_number = True
        elif is_number:
            return int(number)

    if is_number:
        return int(number)

    return None


def get_any_number(string: str) -> int | None:
    """
    Extract the first number (include negative) from a given string
    Args:
        string (str): Input string that may contain digits.

    Returns:
        int | None: The first integer found in the string,
        or None if no integer is present.

    """
    number = ''
    is_number = False
    for i, c in enumerate(string):
        if c.isdigit() and int(c) > 0:
            if i > 0 and string[i - 1] == '-':
                number += string[i - 1]
            number += c
            is_number = True

        elif is_number:
            return int(number)

    if is_number:
        return int(number)

    return None


print(get_any_number('rdg-sdcsd09'))
