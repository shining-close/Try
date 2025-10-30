import numpy as np
import matplotlib.pyplot as plt

A = np.array([[15,35,45],[60,59,67],[50,78,99]])

print(np.trace(A))

print(np.linalg.inv(A))

x = np.array([10, 2, 30, 45])
print("Original array:")
print(x)
print(np.all(x))
print(np.any(x))

m = np.array([45, 67, 23])
n = np.array([56, 23, 89])

print(m)
print(n)

print(np.greater(m, n))
print(np.greater_equal(m, n))
print(np.less(m, n))
print(np.less_equal(m, n))

x = np.arange(0, 5*np.pi, 0.2)
y = np.sin(x)
print("Plot the points:")
plt.plot(x, y)
plt.show()

array1 = np.array([1,2,3,4])
array2 = array1
print(array2)

array1[2 ] = 0
print(array2)

array3 = array1[0:2]
print(array3)
array1[0] = 0
print(array3)

array4 = np.array([11,22,33,44])
array5 = array4.copy()
print(array5)
array4[0] = 0
print(array5)

print("a*b")
a = np.arange(4) #[1,2,3,4]
b = np.arange(4,8)#[4,5,6,7]
print(a * b)