'''
编写一个Python程序，在x轴、y轴上添加适当的标签并设置标题，绘制一条直线。y的值应为x的两倍。x的范围：1到30。
'''

import matplotlib.pyplot as plt

X = range(1, 30)
Y = [value * 2 for value in X]
print("Values of X:")
print(*range(1,30))
print("Values of Y (twice of X):")
print(Y)
# Plot lines and/or markers to the Axes.
plt.plot(X, Y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title
plt.title('Draw a line.')
# Display the figure.
plt.show()