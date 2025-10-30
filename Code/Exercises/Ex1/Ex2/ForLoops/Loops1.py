"""
1 - Write a programme that asks the user to enter their name and a number. If the number is less
than 10, then display their name that number times; otherwise, display the message “Too high”
three times.
"""

name = input("Enter your name: ")
num = int(input("Enter a number: "))

if num < 10:
    for i in range (0, num):
        print(f"This is your name: {name}")
else:
    for i in range (0, 3):
        print("Too high")

'''
Enter your name: guan
Enter a number: 3
This is your name: guan
This is your name: guan
This is your name: guan
'''

'''
Enter your name: liu
Enter a number: 19
Too high
Too high
Too high
'''