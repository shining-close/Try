"""21 - Create an array which will store a list of integers. 
Generate five random numbers and store them in the array. 
Display the array (showing each item on a separate line)."""
import random
from array import *

nums = array('i', [])

for i in range(0, 5):
    num = random.randint(0, 100)
    nums.append(num)

print(nums)

for i in range(0, len(nums)):
    print(nums[i])