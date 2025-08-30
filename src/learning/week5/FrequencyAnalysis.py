"""
File: FrequencyAnalysis.py
Author: Shiqi Su
Date: 2025-08-30 21:33
Description:
"""

class FrequencyNumber:
    """
    A class
    """
def letter_frequency(message: str) -> dict[str, int]:
    """
    Calculate the frequency of each letter in a given message.

    This function analyzes the input string and counts how many times each
    alphabetical character appears. The function is case-insensitive,
    treating uppercase and lowercase letters as the same character.
    Non-alphabetical characters are ignored.

    Args:
        message (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary where the keys are uppercase letters
        and the values are the number of times those letters appear in the
        input message.

    """
    freq = {}
    for i in message.upper():
        if i not in freq:
            freq[i] = 0

        freq[i] += 1
    return freq


def max_letter(freq: dict[str, int]) -> list[str]:
    """
    Find the letter with the highest frequency.

    This function takes a dictionary mapping letters to their occurrence
    counts and returns the letter with the maximum frequency. In the case of
    a tie, any one of the most frequent letters is returned.

    Args:
        freq (dict[str, int]): A dictionary where keys are letters (str) and
        values are their frequencies (int).

    Returns:
        list[str]: The all letters with the highest frequency.
    """
    if not freq:
        return []
    max_num = max(freq.values())
    max_frequency = []
    for i in freq:
        if freq[i] == max_num:
            max_frequency.append(i)
    return max_frequency



print(max_letter(letter_frequency('')))