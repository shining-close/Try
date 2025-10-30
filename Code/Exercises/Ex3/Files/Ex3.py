'''
练习3-（函数和.csv文件）创建以下菜单：
1）添加到文件
2）查看所有记录
3）退出程序输入您的选择编号：
如果用户选择1，允许他们添加到名为Salaries.csv的文件中，该文件将存储他们的姓名和工资。
如果他们选择2，则应显示Salarie.csv文件中的所有记录。如果他们选择3，它应该停止程序。
如果他们选择了错误的选项，他们应该会看到一条错误消息。他们应该继续返回菜单，直到选择选项3。
'''

import csv

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter name: ")
    salary = int(input("Enter Salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()

def viewrecords():
    file = open("salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

tryagain = True
while tryagain == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()
    selection = input("Enter the number of your selection: ")
    if selection == "1":
        addtofile()
    elif selection == "2":
        viewrecords()
    elif selection == "3":
        tryagain = False
    else:
        print("Incorrect option")

