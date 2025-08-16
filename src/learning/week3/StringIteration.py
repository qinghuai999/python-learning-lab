def occurrences(bs: str, cs: str) -> int:
    """
    Takes two string arguments and returns
    the number of times a character from cs occurs in bs
    Args:
        bs (str): This is a base value
        cs (str): This is a comparison value

    Returns:
        int: The number of times the cs value occurs in bs.
    """
    count = 0
    for i in bs:
        for j in cs:
            if i == j:
                count += 1
                break
    return count
print(occurrences('aaa', 'a'))