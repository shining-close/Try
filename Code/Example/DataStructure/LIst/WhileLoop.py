data = [0, -1, 4, 1, 0]

i = 0
while i < len(data) and data[i] <= 0:
    i = i + 1

if i < len(data):
    print(f"the first positive number is at index {i} and is {data[i]}")
else:
    print(f"The list does not contain a positive number")