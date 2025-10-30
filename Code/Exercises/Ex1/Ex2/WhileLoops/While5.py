"""
5 - Create a variable called compnum and set the value to 50. 
Ask the user to enter a number. 
While their guess is not the same as the compnum value, tell them if their guess is too high or too low 
and ask them to have another guess. 
If they enter the same value as compnum, display the message
“Well done, you took [count] attempts”.
"""

compnum = 50
count = 0

num = int(input("Guess a number: "))

while num != compnum:
    if num < compnum:
        print("Your number is too low.")
        num = int(input("Guess a new number: "))
        count += 1
    else:
        print("Your number is too high.")
        num = int(input("Guess a new number: "))
        count += 1

print(f"Well done, you took {count} attempts.")

'''
Guess a number: 20
Your number is too low.
Guess a new number: 60
Your number is too high.
Guess a new number: 54
Your number is too high.
Guess a new number: 50
Well done, you took 3 attempts
'''