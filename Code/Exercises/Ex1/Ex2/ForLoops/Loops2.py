"""
2 - Set a variable called total to 0. Your programme should ask the user to enter five numbers and
after each input, ask them if they want that number to be included. If they do, the programme
should then add the number to the total. If they do not want it included, the programme shouldn’t
add the number to the total. After the user has entered all five numbers, display the total.
"""

total = 0

print("Only can input 5 numbers")



for i in range(0, 5):
    num = int(input("Enter a number: "))
    plus = input("Do you want to plus it to total?(yes/no) ").lower()

    if plus == 'yes':
        total = total + num
    else:
        total = total

print("The total is:", total)

'''
Only can input 5 numbers
Enter a number: 2
Do you want to plus it to total?(yes/no) yes
Enter a number: 2
Do you want to plus it to total?(yes/no) yes
Enter a number: 2
Do you want to plus it to total?(yes/no) yes
Enter a number: 2
Do you want to plus it to total?(yes/no) yes
Enter a number: 2
Do you want to plus it to total?(yes/no) yes
The total is: 10
'''

'''
Only can input 5 numbers
Enter a number: 3
Do you want to plus it to total?(yes/no) no
Enter a number: 3
Do you want to plus it to total?(yes/no) no
Enter a number: 3
Do you want to plus it to total?(yes/no) no
Enter a number: 3
Do you want to plus it to total?(yes/no) no
Enter a number: 3
Do you want to plus it to total?(yes/no) yes
The total is: 3
'''