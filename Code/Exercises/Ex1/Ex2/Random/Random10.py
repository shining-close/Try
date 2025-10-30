"""
10 – Write a programme that randomly chooses either heads or tails (“h” or “t”). 
The programme asks the user to make a choice. 

If their choice is the same as the randomly selected value, 
display the message “You win”, 
otherwise display “Bad luck”. 

At the end, tell the user if the computer selected heads or tails.
"""

import random

select = random.choice(["h", "t"])

choose_user = input("Enter your select from heads and tails(h/t): ")

if select == choose_user:
    print("You win. \n")
else:
    print("Bad luck. \n")

if select == 'h':
    print(f"The computer select heads.")
else:
    print(f"The computer select tails.")
