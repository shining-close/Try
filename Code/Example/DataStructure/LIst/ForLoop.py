data = [2.71, 2.14, 1.67, 1.62]
total = 0

# Select all items from the data list plus
for value in data:
    total = total + value

    print(f"The total is: {total}.")

print("\n")

data2 = [2.71, 2.14, 1.67, 1.62, ]
# Find the largest item and it's index
largest_pos = 0

for i in range(1, len(data)):   # Start from 1 and end at 3, not 4
    if data[i] > data[largest_pos]:
        largest_pos = i

print(f"The largest value is: {data[largest_pos]}, which is at index {largest_pos}")

print("\n")

# Find the largest item and it's index
smallest_pos = 0

length = len(data)
print(f"The length of data is {length}")

# Here is only for loop, means loop 4 times, have no relation with the item in data list
for i in range(1, len(data)):   
    if data[i] < data[smallest_pos]:
        smallest_pos = i

print(f"The largest value is: {data[smallest_pos]}, which is at index {smallest_pos}")