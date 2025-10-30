'''
任务10：编写一个Python程序，显示编程语言流行度的条形图。在每个条形上方附加文本标签显示其流行度（浮点值）
'''

import matplotlib.pyplot as plt

x = ['Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
popularity = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n" + "IEEE survey 2019")
plt.xticks(x_pos, x)

# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%f' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
plt.show()

'''
任务11：编写一个Python程序来创建编程语言流行度的饼图
'''
import matplotlib.pyplot as plt

languages = 'Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#'
popularity = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd","#8c564b","#8c364b"]

# explode 1st slice
explode = (0.1, 0, 0, 0,0,0,0)
# Plot
plt.pie(popularity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


'''
任务12：编写一个Python程序，创建一个显示编程语言流行度的饼图。饼图应有三个扇区。
'''

import matplotlib.pyplot as plt

languages = 'Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#'
popularity = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd","#8c564b","#8c364b"]

# explode 1st slice
explode = (0.1, 0, .2, 0, .1, 0, 0)
# Plot
plt.pie(popularity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Popularity of Programming Language\n" + "IEEE survey 2019")
plt.show()

'''
任务13：从以下DataFrame创建条形图：
'''

from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

a = np.array([[10,40,39,30,39],[80,38,24,33,50],[80,36,90,25,44],[70,45,30,69,15],[25,45,39,30,55]])
df = DataFrame(a, columns=['a','b','c','d','e'], index=[2,4,6,8,10])

df.plot(kind='bar')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()


'''
任务14：编写一个Python程序，在同一图形上创建带误差条的条形图。
'''
import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (54.74, 42.35, 67.37, 58.24, 30.25)
menStd = (4, 3, 4, 1, 5)
# the x locations for the groups
ind = np.arange(N)
# the width of the bars
width = 0.35

plt.bar(ind, menMeans, width, yerr=menStd, color='red')
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

'''
任务15：编写一个Python程序，创建带有误差条的堆叠条形图，使用bottom将女性的条形叠加在男性的条形上。
'''
import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (22, 30, 35, 35, 26)
womenMeans = (25, 32, 30, 35, 29)
menStd = (4, 3, 4, 1, 5)
womenStd = (3, 5, 2, 3, 3)
# the x locations for the groups
ind = np.arange(N)
# the width of the bars
width = 0.35

p1 = plt.bar(ind, menMeans, width, yerr=menStd, color='red')
p2 = plt.bar(ind, womenMeans, width,
bottom=menMeans, yerr=womenStd, color='green')

plt.ylabel('Scores')
plt.xlabel('Groups')
plt.title('Scores by group\n' + 'and gender')
plt.xticks(ind, ('Group1', 'Group2', 'Group3', 'Group4', 'Group5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

'''
任务16：编写一个Python程序，绘制一个散点图，使用X和Y的随机分布并将它们互相绘制。
'''

import matplotlib.pyplot as plt
from pylab import randn

X = randn(200)
Y = randn(200)
plt.scatter(X, Y, color='r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

'''
任务17：编写一个Python程序，使用随机分布绘制不同大小的球的散点图。
'''

import math
import random
import matplotlib.pyplot as plt

# create random data
no_of_balls = 25
x = [random.triangular() for i in range(no_of_balls)]
y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
colors = [random.randint(1, 4) for i in range(no_of_balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(no_of_balls)]

# draw the plot
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

'''
任务19：编写一个Python程序，绘制一个散点图比较Java和Python的两科成绩。
'''

import matplotlib.pyplot as plt
import pandas as pd

java_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
python_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(marks_range, java_marks, label='Java marks', color='r')
plt.scatter(marks_range, python_marks, label='Python marks', color='g')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()