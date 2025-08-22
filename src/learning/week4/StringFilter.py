"""
File: StringFilter.py
Author: Shiqi Su
Date: 2025-08-22 11:55
Description: Return a copy of the string 'bs' with all characters found in 'cs' removed.
"""
def filter_string(bs: str, cs: str) -> str:
    """
    Return a copy of the string 'bs' with all characters found in 'cs' removed.

    This function iterates through each character in 'bs' and builds a new string
    that excludes any characters present in 'cs'. The filtering is case-sensitive.

    Args:
        bs (str): The base string to be filtered.
        cs (str): A string containing the characters to remove from 'bs'.

    Returns:
        str: A new string with all characters from 'cs' removed from 'bs'.
        If all characters in 'bs' are removed, an empty string is returned.
    """
    new_str = ''

    for i in bs:
        if -1 == cs.find(i):
            new_str += i

    return new_str

print(filter_string('hello', 'world'))