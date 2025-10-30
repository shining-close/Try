'''
练习7–使用电话簿数据库，编写一个程序，显示以下菜单
主菜单
1）查看电话簿
2）添加到电话簿
3）搜索姓氏
4）从电话簿中删除联系人
5）退出输入您的选择
如果用户选择1，他们应该能够查看整个电话簿。如果他们选择2，则应允许他们向电话簿中添加新用户。
如果他们选择3，它应该要求他们提供一个姓氏，然后只显示具有相同姓氏的人的记录。
如果他们选择4，它应该要求一个ID，然后从表中删除该记录。如果他们选择5，它应该结束该计划。
最后，如果他们从菜单中输入了错误的选择，程序应该显示一条合适的消息。他们应该在每次操作后返回菜单，直到选择5。
'''

import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter first name: ")
    newsname = input("Enter surname: ")
    newpnum = input("Enter phone number: ")
    cursor.execute("""INSERT INTO Names (id,firstname,surname,phonenumber)
    VALUES (?,?,?,?)""", (newid,newfname,newsname,newpnum))
    db.commit()

def selectname():
    selectsurname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)

def deletedata():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("PhoneBook1.db") as db:
    cursor = db.cursor()

def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()

        if selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect selection entered")

main()
db.close()