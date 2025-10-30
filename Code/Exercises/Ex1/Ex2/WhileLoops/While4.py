"""
4 - Write a programme that asks the user to enter a number and then enter another number. 
The programme should add these two numbers together and then ask if they want to add another number. 
If the user enters “y”, the programme will ask them to enter another number and will keep
adding numbers until the user stops answering “y”. 
Once the loop has stopped, display the total.
"""

total = 0

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

total = num1 + num2 

process = input("Do you want to enter another number?(y/n)").lower()

while process == 'y':
    num3 = int(input("Enter a new number: "))
    total = total + num3
    process = input("Do you want to enter another number?(y/n)").lower()

print("The total is: ", total)


'''
Enter a number: 2
Enter a number: 3
Do you want to enter another number?(y/n)n
The total is:  5
---------------------
Enter a number: 2
Enter a number: 3
Do you want to enter another number?(y/n)y
Enter a new number: 3
Do you want to enter another number?(y/n)n
The total is:  8
---------------------
Enter a number: 2
Enter a number: 3
Do you want to enter another number?(y/n)y
Enter a new number: 4
Do you want to enter another number?(y/n)y
Enter a new number: 5
Do you want to enter another number?(y/n)y
Enter a new number: 6
Do you want to enter another number?(y/n)n
The total is:  20
'''