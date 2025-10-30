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


'''
编写一个Python程序绘制两条或多条带有图例、不同宽度和颜色的线。示例代码：
'''

import matplotlib.pyplot as plt

# Line 1 points
x1 = [10,20,30,70,30]
y1 = [20,40,10,5,10]
# Line 2 points
x2 = [10,20,30,70,30]
y2 = [40,10,30,5,65]

# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title
plt.title('Two or more lines with different widths and colors with suitable legends ')

# Plot lines
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')

# show a legend on the plot
plt.legend()
plt.show()


'''
Task4: 编写一个程序以生成以下输出
'''

import matplotlib.pyplot as plt

# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')

# Plot lines and/or markers to the Axes.
plt.plot(x1,y1, color='red', linewidth = 3,  label = 'red-dotted',linestyle='dotted')
plt.plot(x2,y2, color='green', linewidth = 5,  label = 'green-dashed', linestyle='dashed')

# Set a title
plt.title("Plot with two or more lines with different styles")
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()


'''
任务5：编写一个Python程序，根据以下x和y值数组绘制具有x和y位置的数量：
'''

import numpy as np
import pylab as pl

# Make an array of x values
x1 = [20, 30, 50, 60, 80]
# Make an array of y values for each x value
y1 = [10, 50, 100, 180, 200]
# Make an array of x values
x2 = [30, 40, 60, 70, 90]
# Make an array of y values for each x value
y2 = [20, 60, 110, 200, 220]

# set new axes limits
pl.axis([0, 100, 0, 230])
# use pylab to plot x and y as red circles
pl.plot(x1, y1, 'b*', x2, y2, 'ro')
# show the plot on the screen
pl.show()


'''
任务6：编写一个Python程序以创建多个图表。
'''

import matplotlib.pyplot as plt
fig = plt.figure()
fig.subplots_adjust(bottom=0.020, left=0.020, top=0.900, right=0.800)

plt.subplot(2, 1, 1)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())

plt.show()

'''
任务7：编写一个Python程序以显示编程语言流行度的条形图。
'''

import matplotlib.pyplot as plt

x = ['Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
popularity = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n" + "IEEE survey 2019")
plt.xticks(x_pos, x)

# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()


'''
任务9：编写一个Python程序来显示编程语言受欢迎程度的柱状图。每个柱子使用不同的颜色。
'''

import matplotlib.pyplot as plt

x = ['Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
popularity = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n" + "IEEE survey 2019")
plt.xticks(x_pos, x)

# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()