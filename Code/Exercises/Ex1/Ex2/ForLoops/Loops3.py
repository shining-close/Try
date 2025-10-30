"""
3 - Write a programme that asks which direction the user wants to count (up or down). If they select
up, then the programme should ask them for the top number and count from 1 to that number. If
the user selects down, the programme should ask them to enter a number below 20 and then count
down from 20 to that number. If the user entered something other than up or down, display the
message “I don’t understand”.
"""

select = input("Select up or down: ").lower()
total = 0

if select == 'up':
    num = int(input("Input the end number: "))
    for i in range(0, num + 1):
        total = total + i
    print("The total is: ", total)
else:
    num = int(input("Enter a number below 20: "))
    if num <= 20:
        for i in range(num, 21):
            total = total + i
        print("The total is: ", total)
    else: 
        print("I don't understand")

'''
Select up or down: up
Input the end number: 4
The total is:  10
-----------------------
Select up or down: down
Enter a number below 20: 19
The total is:  39
-----------------------
Select up or down: down
Enter a number below 20: 21
I don't understand
'''
