"""
File: GuessNumber.py
Author: Shiqi Su
Date: 2025-08-08 20:33
Description: Write a program that asks a user to guess a number between 1 and 100. The program should
generate a random number and repeatedly ask the user to input a number until they guess
the correct number. When they guess the correct number, the program should output
Congratulations! and then terminate. The user may give up by entering -1 and the program
will output the number the user was trying to guess and then terminate.
"""
import random
print('Try to guess the number I am thinking of between 1 and 100.')
guess_times = 0
sys_number = 65
# generate a random number
print(random.randint(1, 100))
# Guess number
while True:
    guess_number = int(input('Please enter your guess: '))
    guess_times += 1
    if -1 == guess_number:
        print('The number you were trying to guess was ', guess_times)
        break
    elif guess_number == sys_number:
        print('Congratulations! You have guessed correctly.')
    else:
        print('Sorry that is not correct.')
