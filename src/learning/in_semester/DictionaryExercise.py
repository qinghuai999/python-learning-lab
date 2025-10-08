"""
File: DictionaryExercise.py
Author: Shiqi Su
Date: 2025-09-03 15:37
Description:
"""
def word_pattern(pattern: str, words: list[str]) -> bool:
    """
    Check if a given list of words follows the same pattern as the
    input string.

    This function ensures that:
      - If pattern[j] == pattern[k], then words[j] == words[k].
      - If pattern[j] != pattern[k], then words[j] != words[k].
    In other words, the mapping between characters in the pattern and words in
    the list must be consistent and bijective (one-to-one and onto).

    Args:
        pattern (str): A string pattern consisting of lowercase letters.
        words (list[str]): A list of words to be matched against the pattern.

    Returns:
        bool: True if the words follow the same pattern, False otherwise.

    """
    # Check the length of pattern and words
    if len(pattern) != len(words):
        return False

    # Storing all elements through dictionary.
    pa_dic = {}
    wo_dic = {}
    for i in range(len(pattern)):
        p = pattern[i]
        w = words[i]
        if p in pa_dic and pa_dic[p] != w:
            return False
        if w in wo_dic and wo_dic[w] != p:
            return False
        pa_dic[p] = w
        wo_dic[w] = p

    return True

print(word_pattern('xoox', ['dog', 'cat', 'cat', 'dog']))