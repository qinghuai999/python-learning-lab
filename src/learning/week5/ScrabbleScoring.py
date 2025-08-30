"""
File: ScrabbleScoring.py
Author: Shiqi Su
Date: 2025-08-30 20:05
Description: Calculating the score of a word.
"""
SCRABBLE_VALUES = (
    ('a', 1), ('b', 3), ('c', 3), ('d', 2), ('e', 1),
    ('f', 4), ('g', 2), ('h', 4), ('i', 1), ('j', 8),
    ('k', 5), ('l', 1), ('m', 3), ('n', 1), ('o', 1),
    ('p', 3), ('q', 10), ('r', 1), ('s', 1), ('t', 1),
    ('u', 1), ('v', 4), ('w', 4), ('x', 8), ('y', 4),
    ('z', 10)
)

class ScrabbleScore:
    """
    A class to handle scrabble scoring.

    Attributes:
        score (dict[str, int]): A dictionary mapping each letter to
        its scrabble score.

    Methods:
        get_score(word: str) -> int:
            Calculate the scrabble score of a given word.
    """
    def __init__(self, values: tuple[tuple[str, int], ...]) :
        """
        Convert (letter, score) pairs into a dictionary.

        This function takes in a tuple of (letter, score) pairs and converts it
        into a dictionary mapping each letter (str) to its scrabble score (int).

        Args:
            values (tuple[tuple[str, int], ...]): A tuple of pairs where each pair
            contains a letter (str) and its scrabble score (int).

        Returns:
            dict[str, int]: A dictionary mapping each letter to its scrabble score.

        """
        self.scores = {}

        for i in values:
            k, v = i
            self.scores[k] = v


    def get_score(self, word: str) -> int:
        """
        Calculate the scrabble score of a given word.

        This function takes a dictionary mapping letters to their scrabble values,
        and a word consisting of lowercase letters, then computes the total
        scrabble score of the word by summing the score of each letter.

        Args:
            word (str): The word to calculate the score for. Assumed to be
            lowercase letters only.

        Returns:
            int: The total scrabble score of the input word.
        """
        total_score = 0
        for i in word:
            total_score += self.scores.get(i, 0)
        return total_score


scrabble = ScrabbleScore(SCRABBLE_VALUES)
print(scrabble.get_score('sfre_'))