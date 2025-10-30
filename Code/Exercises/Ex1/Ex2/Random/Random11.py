"""
11 - Write a programme that randomly chooses a number between 1 and 5. 

The programme should ask the user to pick a number. 

If they guess correctly, display the message “Well done”, 
otherwise the programme should tell them if they are too high or too low 
and should ask them to pick a second number. 

If they guess correctly on their second guess, display the message “Correct”, 
otherwise display “You lose”.
"""

import random

num_comp = random.randint(1, 5)

num_user = int(input("Guess a number: "))

if num_user == num_comp:
    print("Well done")
else: 
    if num_user < num_comp:
        print("Your number is too low")
    else:
        print("Your number is too high")
    num_user2 = int(input("Guess a new number: "))

    if num_user2 == num_comp:
        print("Correct")
    else:
        print("You lose")

'''
Guess a number: 3
Well done
-----------
Guess a number: 4
Your number is too high
Guess a new number: 2
You lose
'''
