def reverseList():
    data = [1.62, 1.41, 3.14, 5.74, 98, 3.45]
    print(data)

    temp = data[2]
    data[2] = data[5]
    data[5] = temp

    print(f"Reverse list: {data} \n")

"""answer:
[1.62, 1.41, 3.14, 5.74, 98, 3.45]
Reverse list: [1.62, 1.41, 3.45, 5.74, 98, 3.14]
"""


def sortList():
    values = []

    line = input("Enter a number (blank line to quit): ")
    while line != "":
        num = float(line)
        values.append(num)

        line = input("Enter a number (blank line to quit): ")

    # sort 降序的方式输出 含有参数reverse=True表示降序False表示升序
    values.sort(reverse=True)  

    for v in values:
        print(v)

"""answer:
Enter a number (blank line to quit): 67
Enter a number (blank line to quit): 09
Enter a number (blank line to quit): 78
Enter a number (blank line to quit): 23
Enter a number (blank line to quit): 90
Enter a number (blank line to quit): 654
Enter a number (blank line to quit): 12
Enter a number (blank line to quit): 
9.0
12.0
23.0
67.0
78.0
90.0
654.0
"""

def main():
    reverseList()
    sortList()

if __name__ == "__main__":
    main()