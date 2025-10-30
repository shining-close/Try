"""
22 - Create two arrays 
(one containing three numbers that the user enters and one containing a set of five random numbers). 
Join these two arrays together into one large array. 
Sort this large array and display it so that each number appears on a separate line.
"""

import random
from array import *

nums = array('i', [])
nums2 = array('i', [])
nums_list = []

# 随机五个
for i in range(0, 5):
    num = random.randint(0, 100)
    nums.append(num)

# 用户输入三个
nums_list = input("Enter 3 numbers: ").split()

for i in range(0, len(nums_list)):
    nums2.append(int(nums_list[i]))

# 拼接
nums.extend(nums2)

# 排序
nums = sorted(nums)

# 换行输出
print(nums)
for i in range(0, len(nums)):
    print(nums[i])
