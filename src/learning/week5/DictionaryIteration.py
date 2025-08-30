"""
File: DictionaryIteration.py
Author: Shiqi Su
Date: 2025-08-30 14:53
Description: Dictionary exercise
"""
from logging import exception, error


def big_key(hash: dict[str, int], x: int) -> list[str]:
    """
    Return all keys whose values are greater than the given threshold.
    Args:
        hash (dict[str, int]): Dictionary mapping string keys to
        integer values.
        x (int): Threshold value for comparison.

    Returns:
        list[str]: A list of keys whose corresponding values are greater
        than x.

    """
    arrays = []
    for i in hash:
        if hash[i] > x:
            arrays.append(i)
    return arrays


def subscript_value(d: dict, key):
    """
    Return the value associated with the given key in the dictionary.
    Cannot use get() method
    Args:
        d (dict): The dictionary containing key-value pairs.
        key: The key whose value needs to be retrieved. It is guaranteed
        that this key exists in the dictionary.

    Returns:
        The value associated with the given key in the dictionary.

    """
    for i in d:
        if i == key:
            return d[key]
    return None


def get_value(dictionary: dict, key):
    """
        Return the value associated with the given key in the dictionary.
        Args:
            d (dict): The dictionary containing key-value pairs.
            key: The key whose value needs to be retrieved. It is guaranteed
            that this key exists in the dictionary.

        Returns:
            The value associated with the given key in the dictionary.

        """
    return dictionary.get(key, -1)


def add_to_dict(d: dict, key_value_pairs: list[tuple]
                ) -> list[tuple]:
    """
    Add or update key-value pairs in the dictionary

    This function takes a dictionary and a list of (key, value) tuples.
    It updates the dictionary with the provided pairs, adding new keys
    or updating the values of existing keys.
    Args:
        d (dict): The original dictionary to be updated.
        key_value_pairs (list[tuple]): A list of tuples, where each tuple
        is of the form (key, value).

    Returns:
        list[tuple]: A list of all key-value pairs in the updated dictionary.

    """
    updated = []
    for k, v in key_value_pairs:
        if k in d:
            updated.append((k, d[k]))
        d[k] = v
    return updated


def add_sizes(strings: list[str]) -> list[tuple[str, int]]:
    """
    Transform a list of strings into a list of (string, length) pairs.

    This function takes a list of strings and returns a new list where
    each element is a tuple. The first item in the tuple is the original
    string, and the second item is the integer length of that string.

    Args:
        strings (list[str]): A list of strings to be processed.

    Returns:
        list[tuple[str, int]]: A list of tuples, where each tuple contains
        a string from the input list and its corresponding length.

    """
    tuple_size = []
    for i in strings:
        tuple_size.append((i, len(i)))
    return tuple_size


def git_digits(cs: str) -> str:
    """
    Find all digits in a string then combine them to a new string.
    Args:
        cs (str): A given string to be split.

    Returns:
        str: A digital string

    """
    digital_number = ''


    for i in cs:
        if i.isdigit():
            digital_number += i
    return digital_number

