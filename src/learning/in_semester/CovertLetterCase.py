"""
File: CovertLetterCase.py
Author: Shiqi Su
Date: 2025-09-04 15:35
Description:
"""
def convert_case(xs: str) -> str:
    """
    Covert the first letter is uppercase, others is lowercase, each word
    divided by space.
    Args:
        xs (str): A given word divided by space

    Returns:
        str: A processed string that each first letter is uppercase.

    """
    in_word = False
    low_xs = xs.lower()
    result = ''

    for letter in low_xs:
        if in_word:
            result += letter
            if letter == ' ':
                in_word = False
        else:
            result += letter.upper()
            in_word = True

    return result