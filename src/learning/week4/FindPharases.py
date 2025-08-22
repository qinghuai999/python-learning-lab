"""
File: FindPhrases.py
Author: Shiqi Su
Date: 2025-08-22 11:55
Description: Find all occurrences of a phrase inside a given string starting from a given index.
"""


def find_phrases(phrase: str, string: str, start: int) -> tuple[int]:
    """
    Find all occurrences of a phrase inside a given string starting from a given index.

    This function searches for all instances of the substring 'phrase' within 'string',
    beginning at the position specified by 'start'. It returns a tuple containing
    the starting indices of each match.

    Args:
        phrase (str): The substring (phrase) to search for.
        string (str): The larger string in which to search for the phrase.
        start (int): The index position in 'string' from which to start searching.

    Returns:
        tuple[int]: A tuple of integer indices where the phrase occurs in the string,
        starting from the given index. If no matches are found, an empty typle is returned.

    Notes:
        - The search is case-sensitive.
        - Overlapping occurrences of the phrase are included.
    """

    # <editor-fold desc="By Myself">
    # arr = ()
    # indecis = string.find(phrase, start)
    # index = indecis + 1
    # if indecis == -1:
    #     return arr
    # arr += indecis,
    # for _ in string[string.find(phrase, index):]:
    #     index = string.find(phrase, index)
    #     if index == -1:
    #         return arr
    #
    #     arr += index,
    #     index += 1
    # return arr
    # </editor-fold>

    # <editor-fold desc="Optimized Version">
    arr = ()
    i = string.find(phrase, start)
    while i != -1:
        arr += i,
        i = string.find(phrase, i + 1)
    return arr


# </editor-fold>

print(dir(str))

print(find_phrases("ab", "abcdabfgab", 8))
