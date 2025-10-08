"""
File: FrequencyLetter.py
Author: Shiqi Su
Date: 2025-09-04 15:46
Description:
"""
def frequent_element(xs: str) -> str:
    """
    Return the character in the string (xs) that occurs most frequently.

    If multiple characters occur with the same highest frequency,
    the one with the smallest index (the earliest occurrence) in xs is
    returned.

    Args:
        xs (str): The input string (non-empty).

    Returns:
        str: The single character that is most frequent in xs.
    """
    count = {}
    for i in xs:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    max_value = max(count.values())



    for ch in xs:
        if count[ch] == max_value:
            return ch



print(frequent_element('AASDSAS'))


