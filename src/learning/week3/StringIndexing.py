def string_indexing(words: str) -> None:
    """
    Input a word, iterate through each character in this word on separate lines.
    Parameters:
        words (str): Input some characters.

    Returns:
        None
    """
    length = len(words)
    if length < 2:
        return

    print(words[0])
    print(words[1])
    print(words[-1])

string_indexing(input('Input a word: '))
