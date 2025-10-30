name = input("Your name: ")

# 用+和, 是不同的
print("Hello, " + name + "!")  # Hello, guan!
print("Hello, ", name, "!\n")    # Hello,  guan !


# 字符串拼接
age = int(input("How old are you?"))
year_of_birth = 2025 - age
print("Your were born in " + str(year_of_birth) + ".")

print("\n")

# 以空格形式在一行输入多个
num1, num2 = input("Enter two integers: ").split()

num1 = int(num1)
num2 = int(num2)

print(f"The sum of {num1} and {num2} is {num1 + num2}.")

print("\n")

# 以中间有, 或者空格的形式输出
print("apple", "banana", "cherry", sep=", ")

print("Hello")
print("World1")

print("Hello ")
print("World2")

print("Hello", end=" ")
print("World3")
