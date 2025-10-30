limit = int(input("Enter an integar: "))

print("The multiples of 3 up to and including", limit, "are: ")
for i in range (3, limit + 1, 3):
    print(i)


print("The subtract 4 from ", limit, "each time are: ")
for i in range (limit , 1, -4):
    print(i)


print("The multiples of 2 from 1 up to and including 10 are: ")
for i in range (1, 10, 2):
    print(i)


word = str(input("Enter a word: "))
print("The words in ", word, "are: ")
for i in word:
    print(i)