"""
25 - Create an array of five numbers between 10 and 100 which each have two decimal places. 
Ask the user to enter a whole number between 2 and 5. 
If they enter something outside of that range,
display a suitable error message and ask them again to try until they enter a valid number. 
Divide each of the numbers in the array by the number entered 
and display the answers shown to two decimal places.
"""

import random
from array import *

nums_array = array('i', [])

# 随机五个数，两位小数
for i in range(0, 5):
    nums_array.append(round(random.randint(10, 100), 2))
    # nums_array.append(float('%.2f' % random.randint(10, 100))) 
    """TypeError: 'float' object cannot be interpreted as an integer"""

print(nums_array)

# 防止不是整数
try:
    num = int(input("Enter a whole number between 2 and 5: "))
except:
    num = int(input("Wrong type, enter a new integer between 2 and 5: "))

# 防止不是2与5之间，并且不是整数
while num < 2 or num > 5:
    try:
        num = int(input("Out of range, enter a new number between 2 and 5: "))
    except:
        num = int(input("Wrong type, enter a new integer between 2 and 5: "))

# 输出
for i in range(0, len(nums_array)):
    print(f"The number {nums_array[i]} devided {num} is {round(nums_array[i]/num, 2)}")



'''
python输入保存两位小数的四种办法:

a = 5.5461
办法一:round(a,2)

办法二:float('%.2f' % a)
相干保举:《Python视频教程》

办法三：‘%.2' %a

办法四：
from decimal import Decimal
Decimal('5.026').quantize(Decimal('0.00'))

'''