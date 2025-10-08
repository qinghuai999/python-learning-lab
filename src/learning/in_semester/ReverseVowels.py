"""
File: ReverseVowels.py
Author: Shiqi Su
Date: 2025-09-03 14:07
Description:
"""
def reverse_vowels(xs: str) -> str:
    """
    Iterate all elements and reverse all vowels in this string.

    Args:
        xs (str): A given string to be processed.

    Returns:
        str: A string reverses all vowels.
    """
    vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'

    # Find all vowels
    vols = []
    for ch in xs:
        if ch in vowels:
            vols.append(ch)

    # Reverse all vowels
    reverse_vo = []
    for v in range(len(vols) - 1, -1, -1):
        reverse_vo.append(vols[v])

    # Rever all elements
    result = []
    cal = 0
    for i in range(0, len(xs)):
        if xs[i] in vowels:
            result.append(reverse_vo[cal])
            cal += 1
        else:
            result.append(xs[i])
    s = ''.join(result)
    return s



xs = 'abcdegi'
print(reverse_vowels(xs))
