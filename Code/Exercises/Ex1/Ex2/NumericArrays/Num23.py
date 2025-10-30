"""
23 - Ask the user to enter five numbers. Sort them in order and present them to the user. 
Ask them to select one of the numbers. Remove it from the original array and save it in a new array.
"""

"""23 -要求用户输入5个数字。将它们按顺序排序并呈现给用户。
让他们选择一个数字。将其从原始数组中删除,并将其保存在新数组中。"""
from array import *

nums = array('i', [])

nums_list = input("Enter 5 numbers: ").split()
nums_list.sort()

for i in range(0, len(nums_list)):
    nums.append(int(nums_list[i]))

print("The five numbers are: ", nums)

num = int(input("The number you want to delete: "))

num_dele = int(nums.pop(nums.index(num)))

numsNew = array('b', [num_dele])
print("The common array is: ", nums)
print("The new array is: ", numsNew)