"""
28 – Change the previous programme to ask the user which row they want displayed. 
Display that row. 
Ask the user which column in that row they want displayed and display the value in held in there. 
Ask the user if they want to change the value and change the data. 
Finally, display the whole row again.
"""

select = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

choose = input("row or column: ").lower()
choose_num = int(input("Which row or column: "))

output = []

if choose == 'row':
    # 其实为二维数组
    '''for i in range(0, 3):
        output.append(select[choose_num-1][i])
    print(output)'''
    print(select[choose_num-1])
    choose_column = int(input(f"Which column in row{choose_num-1} want displayed: "))
    print(select[choose_num-1][choose_column-1])
    change = input("Change it or not: ").lower()

    if change == 'yes':
        change_num = int(input("Enter a new number: "))
        select[choose_num-1][choose_column-1] = change_num
        print(select[choose_num-1])
    elif change == 'no' :
        print(select[choose_num-1])
    else: 
        print("You chould enter yes or no")

   
elif choose == 'column':
    for i in range(0, 4):
        output.append(select[i][choose_num-1])
    print(output)
else:
    print("Wrong word!")