"""
File: FileDict.py
Author: Shiqi(Kiki) Su
Date: 2025-09-14 23:03
Description:
"""
def get_lines(filename: str) -> dict[int, str]:
    """12345"""
    """
    Return a dictionary containing each line in the file as values
    and the corresponding line number as keys.
    Args:
        filename (str): The file name, including a path of the file to be
        opened.

    Returns:
        dict[int, str]: Dictionary containing the contents of the file.

    """
    result = {}
    with open('Out_filename.txt', 'r') as file:
        for row, line in enumerate(file):
            result[row] = [line]
    return result

print(get_lines('Out_filename.txt'))


def freq_count(filename: str) -> dict[str, int]:
    """
    Return the frequency count of characters occurring in a file.
    Args:
        filename (str): The file name including a path of the file to be
        open.

    Returns:
        dict[str, int]: Frequency of each character occurring in the file.

    """
    result = {}
    with open('Out_filename.txt', 'r') as file:
        for row in file:
            for i in row:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1
    return result

print(freq_count('Out_filename.txt'))

