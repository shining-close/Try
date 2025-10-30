"""
12 – Write a programme that displays five colours and asks the user to pick one. 
If they pick the same as the programme has chosen, say “Well done”, 
otherwise display a witty answer which involves the correct colour, 
e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE
right now”. 

The programme should ask them to guess again; 
if the user has still not got it right, it keeps giving them the same clue 
and it asks the user to enter a colour until they guess it correctly.
"""

import random

colour = random.choice(["Blue", "Black", "Green", "White", "Red"]).lower()
colour_cos = input("Guess a colour: ")

while colour_cos != colour:
    print(f"I bet you are {colour.upper()} with envy")
    colour_cos = input("Try once again: ")

print("Well done")

'''
Guess a colour: red
I bet you are WHITE with envy
Try once again: white
Well done
---------------------
Guess a colour: red
I bet you are GREEN with envy
Try once again: red
I bet you are GREEN with envy
Try once again: green
Well done
'''