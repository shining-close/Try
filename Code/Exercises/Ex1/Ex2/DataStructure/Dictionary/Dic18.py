"""18 - Create a programme that asks the user to enter four of their favourite foods and store them in a dictionary 
so that they are associated with keys starting from 1. 

Display the dictionary in full, showing the key-value pairs. 

The programme should ask the user which key-value pair they want to get rid of and remove it from the dictionary. 
Finally, the programme should sort the remaining data and display the dictionary"""

foods_list = input("Enter four foods: ").split()

foods_dic = {}

# 判断输入是否为四个，保证字典的最初长度是4
while len(foods_list) != 4:
    if len(foods_list) < 4:
        foods = input(f"Too small, enter {4 - len(foods_list)} more foods: ").split()
        for i in range(0, len(foods)):
            foods_list.append(foods[i])
    else:
        foods = input(f"Too large, delete {len(foods_list) - 4} more foods: ").split()
        for i in range(0, len(foods)):
            del foods_list[foods_list.index(foods[i])]

# 如果是四个
for i in range(0, len(foods_list)):
    foods_dic[i+1] = foods_list[i]

print("the dictionary in full")
print(foods_dic, "\n")

select = input("Want to delete one? (yes/no) ").lower()

while select != 'no' and len(foods_dic) != 0:
    key, value = input("Which pair want to delete: ").split(":"+" ")
    foods_dic.pop(int(key))   # 切记要int(key),因为input的输入为str
    select = input("Want to delete one? (yes/no) ").lower()

if len(foods_dic) == 0:
    print("There are no pairs.")
else:
    foods_dic = sorted(foods_dic.items(), key=lambda x: x[0])   # 排序
    print(f"The dictionary is: {dict(foods_dic)}")

'''
Enter four foods: a b c
Too small, enter 1 more foods: d
the dictionary in full
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

Want to delete one? (yes/no) yes
Which pair want to delete: 3: 'c'
Want to delete one? (yes/no) no
The dictionary is: {1: 'a', 2: 'b', 4: 'd'}
'''