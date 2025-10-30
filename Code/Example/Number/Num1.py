number1 = float(input("Enter a number: "))

if number1 >= 20:
    if number1 <= 50:   # 原题中为 number1 =< 50
                        # 
        results = "This is between 20 and 50"
    else:
        results = "This is over 50"
else:
    results = "This is below 20"

print(results)

'''
    if number1 =< 50:
               ^
SyntaxError: invalid syntax
'''