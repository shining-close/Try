import numpy as np

# 一维数组
lst1 = [1,2,3,4,5,6] # 定义一个列表
a1=np.array(lst1) # 创建一维数组
print('a1=',a1) # 打印一维数组
lst2 = [[1,2,3],[4,5,6]] # 定义一个嵌套列表
a2 = np.array(lst2) # 创建二维数组
print('a2=\n',a2) # 打印二维数组


# 二维数组
arr_data = np.array([[0]*3]*2)  #存储该产品的时间序列 可以看到3为列数，2为行数
print(arr_data)


#直接利用numpy库的函数，其中zeros（值为0）可换成empty（值为空），ones （值为1）
#2为行数，3为列数
arr = np.zeros((2,3), dtype=np.float64)
print(arr)

# 三维数组

import numpy as np
arr_data = [None]*4  #纵向深度也就是第三维是4，有4层数组  
for i in range(len(arr_data)):
    arr_data[i] = [0]*2   #行数
    for j in range(len(arr_data[i])):
        arr_data[i][j] = [0]*3   #列数
array_data = np.array(arr_data)  #将列表类型转为数组类型
print(array_data.shape)
print(array_data)


arr = np.zeros((4,2,3), dtype=np.float64)
print(arr)