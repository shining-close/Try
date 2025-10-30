import numpy as np

# Create an array of integers from 10 to 20 (inclusive)
arr = np.arange(10, 21)

# Print the array
print(arr)


# Create a 3x3 array (example with random integers between 1 and 10)
arr = np.random.randint(1, 11, size=(3, 3))

print("Original array:")
print(arr)
print()

# Save the array to a text file
np.savetxt('3x3_array.txt', arr, fmt='%d')  # fmt='%d' specifies integer format
print("Array saved to '3x3_array.txt'")
print()

# Load the array from the text file
loaded_arr = np.loadtxt('3x3_array.txt', dtype=int)

print("Loaded array:")
print(loaded_arr)


array1 = np.array([[3, 5, 1],
                   [2, 3, 5],
                   [1, 3, 1]])

array2 = np.array([[8, 5, 1],
                   [2, 9, 4],
                   [2, 10, 5]])

addition = array1 + array2
print("Addition:")
print(addition)

subtraction = array1 - array2
print("\nSubtraction:")
print(subtraction)

matrix_product = np.dot(array1, array2)
print("\nMatrix Product:")
print(matrix_product)