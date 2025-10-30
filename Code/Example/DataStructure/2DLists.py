grades = [[45, 67, 57], [65, 58, 34], [23, 89, 35], [56, 76, 87]]
print(grades, "\n")   # 不能用grades + "\n", 因为grades不是字符串
# [[45, 67, 57], [65, 58, 34], [23, 89, 35], [56, 76, 87]] 

'''
    print(grades+"\n")
          ~~~~~~^~~~~
TypeError: can only concatenate list (not "str") to list
'''

grades = [{"Ma": 45, "En": 67, "Fr": 57}, {"Ma": 65, "En": 58, "Fr": 34}, {"Ma": 23, "En": 89, "Fr": 35}, {"Ma": 56, "En": 76, "Fr": 87}]
print(grades[0]["En"], "\n")
# 67

grades = {"Paul": {"Ma": 45,"En": 67,"Fr": 57}, "Mary": {"Ma": 23, "En": 89, "Fr": 35}}
print("The grade for Paul's maths exam is: ", grades["Paul"]["Ma"], "\n")
# The grade for Paul's maths exam is:  45

print("This is Mary's exam result: ", grades["Mary"], "\n")
# This is Mary's exam result:  {'Ma': 23, 'En': 89, 'Fr': 35}

grades["Mary"]["Fr"] = 55
print("This is Mary's exam result: ", grades["Mary"], "\n")

grades["Rita"] = {"Ma": 70, "En": 69}
print(grades, "\n")

for name in grades:
    print((name), grades[name]["En"])