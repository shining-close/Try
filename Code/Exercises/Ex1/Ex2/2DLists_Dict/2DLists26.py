"""
26 – Create the following using a simple 2D list 
and ask the user to select a row and a column and display that value.
"""

select = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

choose = input("row or column: ").lower()
choose_num = int(input("Which row or column: "))

output = []

if choose == 'row':
    for i in range(0, 3):
        output.append(select[choose_num-1][i])
    print(output)
elif choose == 'column':
    for i in range(0, 4):
        output.append(select[i][choose_num-1])
    print(output)
else:
    print("Wrong word!")