"""24 - Display an array of five numbers. 
Ask the user to select one of the numbers. 
Once they have selected a number, 
display the position of that number in the array. 

If they enter something that is not in the array, 
ask them to try again until they select a relevant number."""

from array import *

nums = array('i', [21, 23, 56, 65, 87])

print("The array: ", nums)

num = int(input("The one select: "))

select = True

if num in nums:
    select = True
    print(f"The position of {num} is {nums.index(num)}.")
else:
    select = False

while select != True:
    print(f"This number {num} is not in array nums.")
    num = int(input("Enter another number: "))
    if num in nums:
        select = True
        print(f"The position of {num} is {nums.index(num)}.")
        break
    else:
        select = False

