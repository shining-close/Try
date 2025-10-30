"""
20 – Write a programme that asks the user for a list of five integers. Store them in an array. Sort the
list and displays it in reverse order.
"""
from array import *

num_list = []
num_list = input("Enter five integers: ").split()

nums = array('b', [])  # arrey 创建时必须要有'a', array() takes at least 1 argument (0 given)
                       # bad typecode (must be b, B, u, w, h, H, i, I, l, L, q, Q, f or d)

for i in range(0, len(num_list)):
    nums.append(int(num_list[i]))   # 'str' object cannot be interpreted as an integer

nums.reverse()
print("This is reversed array: ", nums)
