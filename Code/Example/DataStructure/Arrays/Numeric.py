from array import *

nums = array('i', [45, 78, 345, 98, 12, 78])   # 这是array.array
print("This is the original array: ", nums)
# This is the original array:  array('i', [45, 78, 345, 98, 12, 78])

newNumber = int(input("Enter a number: "))
nums.append(newNumber)
print("This is the array with the new number: ", nums)
# This is the array with the new number:  array('i', [45, 78, 345, 98, 12, 78, 9])

nums.reverse()   # 注意：没有参数
print("This is the reversed array: ", nums)
# This is the reversed array:  array('i', [9, 78, 12, 98, 345, 78, 45])

nums = sorted(nums)   # 注意：不同于List中的.sort()，这里是sorted(含参数)
print("This is the sorted array: ", nums)
# This is the sorted array:  [9, 12, 45, 78, 78, 98, 345]
'''
AttributeError: 'array.array' object has no attribute 'sorted'
对象错误: 指不存在sorted这个对象
没有num.sorted(nums)这个写法
只有nums = sorted(nums)
'''


nums.pop()
print("This is the array after removing the last number: ", nums)
# This is the array after removing the last number:  [9, 12, 45, 78, 78, 98]


newArray = array('i', [])

more = int(input("How many numbers in total do you want to add? "))
for y in range (0, more):
    newValue = int(input("Enter a number: "))
    newArray.append(newValue)
print("This is the newArray array after adding the items: ", newArray)
# This is the newArray array after adding the items:  array('i', [9, 5, 3, 2])


nums.extend(newArray)   # 将两个array拼接起来
print("This is the nums array after joining it with newArray:", nums)
# This is the nums array after joining it with newArray: [9, 12, 45, 78, 78, 98, 9, 5, 3, 2]


# 默认移除的是这个数的在array中的第一个数
getRid = int(input("Enter the number you want to remove: "))
nums.remove(getRid)
print("This is the array aftering removing the number: ", nums)
# This is the array aftering removing the number:  [12, 45, 78, 78, 98, 9, 5, 3, 2]

# 使用.count()直接计数
print("78 appears", nums.count(78), "times")
# 78 appears 2 times
print("This is the array after removing the requested number ", nums)
# This is the array after removing the requested number  [12, 45, 78, 78, 98, 9, 5, 3, 2]

'''
1. list，不限定数据类型。使用起来非常灵活，但带来的缺点是速度相对较慢，因为对每一个元素要检查数据类型；
myList = [i for i range(10)]
2. array.array，限定数据类型。限制了灵活性，相对速度比较高；同时array只是将存储的数据看成数组或二维数组，而数组并没有看成矩阵，也没有配备向量或矩阵相关的运算；
myArray = array.array('i', [i for i range(10)])
3. numpy.array应运而生，操作同list、array.array；与array.array一样只存储一种数据类型，可以使用dtype属性查看
myNpArray = numpy.array([i for i range(10)])
'''