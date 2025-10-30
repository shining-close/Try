results = {"pass": 0, "fail": 0}
print(results)   # {'pass': 0, 'fail': 0}

results["withdrawal"] = 1
print(results)   # {'pass': 0, 'fail': 0, 'withdrawal': 1}

results["pass"] = 3
results["fail"] = results["fail"] + 1
print(results)   # {'pass': 3, 'fail': 1, 'withdrawal': 1}

print(results["fail"])
print(results["pass"])
print(results["withdrawal"])

"""
{'pass': 0, 'fail': 0}
{'pass': 0, 'fail': 0, 'withdrawal': 1}
{'pass': 3, 'fail': 1, 'withdrawal': 1}
1
3
1
"""

# 将字典中的Key,value转化为表格
a = list(results.keys())
print(a)   # ['pass', 'fail', 'withdrawal']
b = list(results.values())
print(b)   # [3, 1, 1]

# 字典长度
print("The length of dic:", len(results))  # The length of dic: 3

# 判断存在与否
x = "pass"
if x in results.keys():
    print("At least one of the key in results is:", x)  # At least one of the value in results is: pass
else:
    print("None of the key in results are:", x)

if "fail" in results.keys():
    print("At least one of the key in results is fail")  # At least one of the value in results is fail
else:
    print("None of the key in results is fail")

y = 3
if y in results.values():
    print("At least one of the value in results is:", y)  # At least one of the value in results is: 3
else:
    print("None of the value in results are:", y)

# 字典删除
# 使用del语句
d = {'a': 1, 'b': 2}
del d['a']
print(d)

# 使用pop方法
d = {'a': 1, 'b': 2}
value = d.pop('a')
print(d)

# 排序(不能直接用sorted, 不然出来的会是列表)
# 字典排序
a = {'a': 3, 'c': 89, 'b': 0, 'd': 34}
# 按照字典的值进行排序
a1 = sorted(a.items(), key=lambda x: x[1])
# 按照字典的键进行排序
a2 = sorted(a.items(), key=lambda x: x[0])
print('按值排序后结果', a1)
print('按键排序后结果', a2)
print('结果转为字典格式', dict(a1))
print('结果转为字典格式', dict(a2))
a3 = sorted(a.values())
print(a3)   # [0, 3, 34, 89]

'''
按值排序后结果 [('b', 0), ('a', 3), ('d', 34), ('c', 89)]
按键排序后结果 [('a', 3), ('b', 0), ('c', 89), ('d', 34)]
结果转为字典格式 {'b': 0, 'a': 3, 'd': 34, 'c': 89}
结果转为字典格式 {'a': 3, 'b': 0, 'c': 89, 'd': 34}
'''