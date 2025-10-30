"""
27 - Using the 2D list in the previous exercise, 
ask the user which row they would like displayed and display just that row.  
Ask them to enter a new value and add it to the end of the row and display row again.
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
    input_new = int(input("Enter a new number in this row: "))
    select[choose_num-1].append(input_new)   
    print(select[choose_num-1])
elif choose == 'column':
    for i in range(0, 4):
        output.append(select[i][choose_num-1])
    print(output)
else:
    print("Wrong word!")

