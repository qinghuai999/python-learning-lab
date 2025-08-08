

import random
"""
Version 1: The program will generate two random 2-digit integers, 
and ask the user what the sum of the two integers is, 
and display whether or not the user is correct. 
If the user is incorrect, also display the correct answer.
"""

# <editor-fold desc="Version 1">
# count = 10
#
# while(0 < count):
#     count -= 1
#     add1 = random.randint(1,99)
#     add2 = random.randint(1, 99)
#
#     print(add1, "+", add2, " = ", end="")
#     answer = int(input())
#     sys_answer = add1 + add2
#     if answer == sys_answer:
#         print("Correct!")
#     else:
#         print('No, the correct answer is ', sys_answer)
# </editor-fold>

"""
Challenge 3: Advanced Academy (Hard!)
Modify the above program so that it also randomly selects an operator from the six options + - * // ** %, 
to test Alice’s abilities with all of them. 
If the ** operator is being used, the exponent should be randomly chosen between 0 and 3, instead of between 10 and 99.
"""
# <editor-fold desc="Version 2">
# Define possible operators
operators = ['+', '-', '*', '//', '**', '%']
count = 10
while(0 < count):
    count -= 1
    symbol = random.choice(operators)
    if symbol == '**':
        para1 = random.randint(0, 9)
        para2 = random.randint(0, 3)
    else:
        para1 = random.randint(10, 99)
        para2 = random.randint(10, 99)

    print(para1, symbol, para2, "= ", end= "")
    users_answer = int(input())
    final_value = eval(f"{para1} {symbol} {para2}")
    if final_value == users_answer:
        print("Correct!")
    else:
        print('No, the correct answer is ', final_value)



# </editor-fold>