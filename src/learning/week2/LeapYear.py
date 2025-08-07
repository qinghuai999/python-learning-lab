from itertools import count

for _ in range(5):
    yearNumber = int(input('Please enter a year: '))
    if (yearNumber % 4 == 0 and yearNumber % 100 != 0) or (yearNumber % 400 == 0):
        print(True)
    else:
        print(False)
