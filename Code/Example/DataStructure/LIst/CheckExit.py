data = []

line = input("Enter a number (blank line to quit): ")
while line != "":
        num = int(line)
        data.append(num)

        line = input("Enter a number (blank line to quit): ")


print(data)

y = int(input("Enter one additional integer: "))

if y in data:
    print("The first", y, "is at index", data.index(y))
else:
    print(y, "is not in the list")

"""
Enter a number (blank line to quit): 12        
Enter a number (blank line to quit): 34
Enter a number (blank line to quit): 7
Enter a number (blank line to quit): 89
Enter a number (blank line to quit): 6
Enter a number (blank line to quit): 
[12, 34, 7, 89, 6]
Enter one additional integer: 7
The first 7 is at index 2
"""