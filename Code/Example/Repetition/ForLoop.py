limit = int(input("Enter an integar: "))

print("The multiples of 3 up to and including", limit, "are: ")
for i in range (3, limit + 1, 3):
    print(i)

'''
The multiples of 3 up to and including 15 are: 
3
6
9
12
15
'''

print("The subtract 4 from ", limit, "each time are: ")
for i in range (limit , 1, -4):
    print(i)

'''
The subtract 4 from  15 each time are:
15
11
7
3
'''
print("The multiples of 3 up to and including 10 are: ")
for i in range (1, 10, 2):
    print(i)
'''
The multiples of 3 up to and including 10 are:
1
3
5
7
9
'''

word = str(input("Enter a word: "))
print("The words in ", word, "are: ")
for i in word:
    print(i)

'''
Enter a word: woed
The words in  woed are: 
w
o
e
d
'''

for i in range(20, 10, -2):
    print(i)