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
