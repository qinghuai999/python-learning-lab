"""
File: DnaManipulation.py
Author: Shiqi Su
Date: 2025-08-22 16:55
Description: Logic thinking exercise.
"""


def is_dna(string: str) -> bool:
    """
    Check if the given string is a valid DNA sequence.

    A valid DNA sequence:
    - Contains only the characters 'A', 'T', 'G' and 'C'
    - Has a length that is a multiple of 3

    Args:
        string (str): The input string representing a potential DNA sequence.

    Returns:
        bool: True if the string is a valid DNA sequence, False otherwise.
    """
    condition = 'ATGC'
    for i in string:
        if condition.find(i) == -1:
            raise ValueError('Invalid DNA sequence')
    if len(string) % 3 != 0:
        raise ValueError('Invalid DNA sequence')
    return True


def reverse_complement(dna: str) -> str | None:
    """
    Compute the reverse complement of a DNA sequence

    The reverse complement is formed by
        1. Replacing each base with its complement:
            - 'A' <-> 'T'
            - 'C' <-> 'G'
        2. Reversing the entire sequence.

    If the input string is not a valid DNA sequence
    (i.e, contains characters other than 'A', 'T', 'G', 'C'),
    the function returns None.

    Args:
        dna (str): The DNA sequence to be processed.

    Returns:
        str | None: The reverse complement of the DNA sequence,
        or None if the sequence is invalid.

    """
    # Check if this dna is valid
    if not is_dna(dna):
        return None

    new_dna = dna[::-1]

    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse_comp = []
    for i in new_dna:
        reverse_comp.append(complement[i])
    reverse_comp = ''.join(reverse_comp)
    return reverse_comp


def print_codons(dna: str) -> list[str] | None:
    """
    Print the codons (groups of three nucleotides) of a DNA sequence.

     This function takes a DNA sequence string and prints each codon
     (a block of three letters) on a new line. If the DNA sequence is invalid,
     meaning its length is not a multiple of three, the function does nothing.

    Args:
        dna (str): A string representing the DNA sequence. Must only
        contain valid DNA characters('A', 'T', 'G', 'C').

    Returns:
        str | None: It returns a block of three letters on a new line.
        Or return None

    """
    # Check if the sequence is valid
    if not is_dna(dna):
        return None
    arr = []

    for i in range(0, len(dna), 3):
        arr.append(dna[i:i + 3])
    new = '\n'.join(arr)
    return new


print(print_codons("AAtGAC"))
