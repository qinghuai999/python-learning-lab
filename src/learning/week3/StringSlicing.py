def slice_from(string: str, start: int, end: int) -> str:
    """
    Returns the characters in string from index start up to,
    but not including, index end.
    Note that this characteristic of including the character at the start index,
    but excluding the one at the end index, is the default slicing behavior.
    Args:
        string (str): Input a string
        start (int): Slice the string from the start parameter.
        end (int): Ending the slice in the end parameter but not including index end.

    Returns:
        str: The part of the string between the start index (inclusive)
        and the end index (exclusive).
    """
    return string[start: end]


def reverse_string(string: str) -> str:
    """
    This function which returns the characters in string in reverse order
    Args:
        string: Input a string

    Returns:
        str: Return a reverse string.
    """
    return string[::-1]


print(reverse_string('abcd'))
