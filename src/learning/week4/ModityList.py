"""
File: ModityList.py
Author: Shiqi Su
Date: 2025-08-22 11:55
Description: Combine adjacent strings in a list into new strings.
"""
def modify(xs: list[str]) -> list[str]:
    """
    Combine adjacent strings in a list into new strings.

    This function takes a list of strings and merges every two adjacent
    strings together into a single string. The result is a new list
    containing these merged strings. If the list has an odd number of
    elements, the final string will be added as is.
    string into a new list
    Args:
        xs (list[str]): A list of string to be combined.

    Returns:
        list[int]: A new list of strings where each element is a
        concatenation of two adjacent strings from the input list.
        If the input list has an odd length, the last string is
        included unchanged.
    """
    result = []
    for i in range(0, len(xs), 2):
        if i + 1 < len(xs):
            merged = xs[i] + xs[i + 1]
        else:
            merged = xs[i]
        result.append(merged)
    return result


print(modify(['a', 'bc', 'qr', 'lpd', 'gyt']))
