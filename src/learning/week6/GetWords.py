"""
File: GetWords.py
Author: Shiqi(Kiki) Su
Date: 2025-09-15 14:17
Description:
"""
def get_words(filename: str) -> list[str]:
    """
    Storing all of the words in a list, and show words that contain 'z'.
    Args:
        filename (str): The file name includes a path of the file to be open.

    Returns:
        list[str]: All words that contain 'z'

    """
    z_words = []
    with open('words.txt') as file:
        for line in file:
            words = line.split()
            for i in words:
                if 'z' in i:
                    z_words.append(i)
    return z_words
print(get_words('words.txt'))


