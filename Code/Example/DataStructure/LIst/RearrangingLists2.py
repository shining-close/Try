# 以空格形式输入一个数组
# 以排列好的行书输出列表
try1 = input("Enter integers: ").split()  # Enter integers: 12 23 34 45
print(try1)  # ['12', '23', '34', '45']

try2 = []

for i in range(0, len(try1)):
    try2.append(int(try1[i]))

# sort()方法，是在原始列表上进行排序，默认是从小到大。
# 该方法含有一个参数：reverse，表示是否反向，若reverse=True 则将其按照从大到小的顺序排序。
try2.sort()
print(try2) # [12, 23, 34, 45]

try2.sort(reverse=True)
print(try2) # [43, 32, 23, 12]

# sorted()函数，对原始列表不作修改，返回一个新的已排序列表
try3 = sorted(try2)
print(try2) # [43, 32, 23, 12]
print(try3) # [12, 23, 32, 43]