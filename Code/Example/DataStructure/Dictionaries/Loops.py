constants = {"pi": 3.14, "e": 2.71, "root": 1.41}

for k in constants:
    print(f"The value associated with {k} is {constants[k]}")

"""
The value associated with pi is 3.14
The value associated with e is 2.71
The value associated with root is 1.41
"""

'''
for v in constants.values():
    print(f"The value is {v}")
'''

total = 0
for i in constants.values():
    total = total + i

print(f"The total is: {total}")   # The total is: 7.26

##########while########
# 使用 While 输入，并判断某个数被输入了几次
counts = {}

while len(counts) < 5:
    s = input("Enter a string: ")

    if s in counts:
        counts[s] = counts[s] + 1
    else: 
        counts[s] = 1

for k in counts:
    print(f"{k} occured {counts[k]} times.")

print(counts)

"""
Enter a string: hello
Enter a string: hi
Enter a string: hell
Enter a string: gcp
Enter a string: hello
Enter a string: hi
Enter a string: world
hello occured 2 times.
hi occured 2 times.
hell occured 1 times.
gcp occured 1 times.
world occured 1 times.
{'hello': 2, 'hi': 2, 'hell': 1, 'gcp': 1, 'world': 1}
"""