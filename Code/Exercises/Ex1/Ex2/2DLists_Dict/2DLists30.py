"""
30 – After gathering the four names, ages and shoe sizes, 
ask the user to enter the name of the person they want to remove from the list. 
Delete this row from the data and display the other rows on separate lines.
"""

grades = {}
grades_single = {}

for i in range(0, 4):
    name = input("Who: ")
    grades_single['name'] = name
    grades_single['age'] = int(input("The age: "))
    grades_single['shoe size'] = int(input("Shoe size: "))

    grades[name] = grades_single
    # 删除完原来的grades_single 新创建的地址与原来的就不一样了，即便是变量名一样
    del grades_single
    grades_single = {}

name_remove = input("Which name to remove: ")
del grades[name_remove]

for name in grades:
    print(grades[name])
    