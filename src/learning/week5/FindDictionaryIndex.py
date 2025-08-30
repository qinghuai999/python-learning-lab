"""
File: FindDictionaryIndex.py
Author: Shiqi Su
Date: 2025-08-29 14:28
Description: Dictionary and index exercise
"""


def char_index(xs: str) -> dict[str, list[int]]:
    """
    There is a string parameter, given a special letter,
    find the index of the letter. If there are several similar letters,
    list all indexes.
    Args:
        xs (str): A string words

    Returns:
        dict[str, list[int]]: Displaying the letter and index
    """

    indexs = {}
    for i, char in enumerate(xs):
        if char in indexs:
            indexs[char].append(i)
        else:
            indexs[char] = [i]
    return indexs


CHARS = 'hello world, baby'
print(char_index(CHARS))


def combine(d1: dict[int, list[int]],
            d2: dict[int, list[int]]) -> dict[int, int]:
    """
    Return the dictionary where each key is in both d1 and d2,
    and sum of the all values.
    Args:
        d1 (dict[int, list[int]]): The first dict data
        d2 (dict[int, list[int]]): The second dic data

    Returns:
        dict[int, int]: The intersection key and sum of value.
    """
    ans = {}
    for key in d1:
        if key in d2:
            ans[key] = sum(d1[key]) + sum(d2[key])
    return ans


d1 = {1: [1, 2], 2: [2, 4, 5], 5: [2]}
d2 = {2: [3], 5: [6, 7]}
print(combine(d1, d2))
