"""
File: AddNumbers.py
Author: Shiqi(Kiki) Su
Date: 2025-09-17 17:19
Description:
"""
def add() -> int:
    """ Prompts the user to enter to integers. Then adds the two
    numbers together and returns the result.
    Output:
        Addition of two entered integers

    """

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Write your code here
    try:
        a = int(num1)
        b = int(num2)
        print(a + b)
    except ValueError:
        print("Invalid number entered")

# do not remove this line
add()