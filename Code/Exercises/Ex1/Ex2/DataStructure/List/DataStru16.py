"""16 - Create a list of four three-digit numbers. 
Display the list to the user, showing each item from the list on a separate line. 
Ask the user to enter a three-digit number. 
If the number they have typed in matches one in the list, 
display the position of that number in the list 
otherwise display the message “That's not in the list”."""
"""创建一个包含四个三位数的数字的列表.
向用户显示列表，将列表中的每个项目显示在单独的一行上。
要求用户输入一个三位数的数字。
如果他们输入的数字与列表中的数字相符，
显示该数字在列表中的位置
否则显示消息“That's not in the list”。"""

list = [123, 234, 345, 456]

for i in range (0, len(list)):
    print(list[i])

num = int(input("Enter a new number: "))

while len(str(num)) != 3:
    num = int(input("You should enter a THREE-digit number: "))


if num in list:
    print(f"The position of {num} in list is {list.index(num)}")
else:
    print(f"That's not in the list")

'''
123
234
345
456
Enter a new number: 46
You should enter a THREE-digit number: 234
The position of 234 in list is 1
'''
    

"""
#请验证输入的列表N_list中的整数是否为三位数, 并返回三位数整数的百位数值
 
N_list = [int(i) for i in input().split(',')] # 将输入数字以逗号分隔形成列表
a=[]                                          # 创建新列表
for i in  N_list:                             # 遍历输入列表
    if len(str(i))==3:                        # 用len()判断列表长度
        a.append(int(i//100))                 # 百位取整,并用x.append()将数字按序添加到列表a中
print(a)                                      # 打印输出a
"""