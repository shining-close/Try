import math
# import // is keyword
# math // is the name of python file contains the function you want 

# Kai Ping Fang
number1 = 4
print("The number is", number1)
print("The square root of", number1, "is", math.sqrt(4), "\n")

# Si Se Wu Ru
number2 = 6.7777
print("The number is", number2)
print("Kai Ping Fang 4 is", round(number2, 2), "\n")

# Ping Fang
number3_1 = 10
number3_2 = 2
number3_3 =  number3_1**number3_2 
print("The number is", number3_1, "de", number3_2, "Ci Fang")
print( number3_1, "de", number3_2, "Ci Fang is", number3_3, "\n")

number4 = 15//2
print("15//2 is", number4)

number5 = 15%2
print("15%2 is", number5)

number6 = 15/2
print("15/2 is", number6)


y = int(input("Enter a number: "))

# If not import math
# It will display: name "math" is not defined
# sqrt mains kai ping fang
z = math.sqrt(y)

print(z)

num = float(input("Enter a try number: "))
print("Display the number rounded to two decimals", round(num, 2))
