test = (1, 2, 3, 4)   #  不能用数字当变量名首字母

_ = [3, 5, 6, 9]   #  可以用_符号做变量名

del (test)  #  NameError: name 'test' is not defined
            #  确实可以直接删除test

print(_)   #  (3, 5, 6, 9)

_.insert(2, '500')   #  'tuple' object has no attribute 'insert'
print(_)             #  [3, 5, '500', 6, 9]  此时的'500'代表的是字符串500

_.insert(2, 500)
print(_)



