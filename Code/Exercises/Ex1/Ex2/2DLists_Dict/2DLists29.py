"""
29 – Ask the user to enter the name age and show size for the four people in a list 
and display the names and ages of all the people in the list but do not show their show size.
"""

grades = {}
grades_single = {}

for i in range(0, 4):
    name = input("Who: ")
    grades_single['name'] = name
    grades_single['age'] = int(input("The age: "))
    grades_single['show size'] = int(input("Show size: "))

    grades[name] = grades_single
    # 删除完原来的grades_single 新创建的地址与原来的就不一样了，即便是变量名一样
    del grades_single
    grades_single = {}

    print(grades)
print(grades)

for name in grades:
    print((name), "'s age is: ", grades[name]["age"])