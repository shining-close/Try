"""
7 - Define a function that will ask the user to enter a number and save it as the variable “num”.
Define another function that will use “num” and count 1 to that number.

"""

def askNum():
    num = int(input("Enter a number: "))
    num1 = plusOne(num)
    print(f"After plus 1, the number = {num1}")


def plusOne(n):
    n += 1
    return n

askNum()

'''
Enter a number: 3
After plus 1, the number = 4
'''