'''
练习5-对一组数字求和
创建一个程序，将用户输入的所有数字求和，同时忽略任何无效数字的输入。
输入每个数字后，您的程序应显示当前总和。它应该在每次非数字输入后显示一条适当的消息，
然后继续对用户输入的任何其他数字求和。当用户输入空白行时退出程序。确保您的程序对整数和浮点数都能正确工作。
'''

# Read the first line of input from the user
line = input("Enter a number: ")
total = 0

# Keep reading until the user enters a blank line
while line != "":
    try:
        # Try and convert the line to a number
        num = float(line)
        # If the conversion succeeds then add it to the total and display it
        total = total + num
        print("The total is now", total)
    except ValueError:
        # Display an error message before going on to read the next value
        print("That wasn't a number.")
    line = input("Enter a number: ")

# Display the total
print("The grand total is", total)