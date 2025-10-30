import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('Code/Team/Team5/tAPP5_company_sales_data.csv')

# Extract data for plotting
months = df['month_number']
total_profit = df['total_profit']

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(months, total_profit, marker='o', linestyle='-', color='b', linewidth=2, markersize=1)

# Set labels and title
plt.xlabel('Month Number', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)
plt.title('Total Profit of All Months', fontsize=14)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

'''----------------------------------------------------------'''

# Example data for task 4 (assuming you have a dictionary of language popularity)
languages = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript', 'R', 'C#']
popularity = [95.5, 45, 40, 35, 90, 60, 78.9]

# Task 4: Horizontal Bar Chart
plt.figure(figsize=(10, 5))
plt.barh(languages, popularity, color=['skyblue', 'red', 'green', 'purple', 'yellow', 'cyan', 'black'])

# Adding labels and title
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

# -------Turn on the grid---------These have been commented out to remove the error
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.5, color='red')
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='black')

# Display the plot
plt.show()

'''---------------------------------------------------------------'''

import matplotlib.pyplot as plt

# 示例数据
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
popularity = [85, 70, 60, 55, 45]

# 创建画布和轴对象
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向条形图
ax.barh(languages, popularity, color='lightblue')

# 设置网格线（重点）
ax.grid(
    axis='both',        # 只显示垂直网格线（与x轴平行）
    linestyle='--',  # 虚线样式
    color='red',    # 灰色
    alpha=0.7,       # 半透明
    linewidth=0.8    # 线宽
)

# 其他样式设置
ax.set_xlabel('流行度', fontsize=12)
ax.set_ylabel('编程语言', fontsize=12)
ax.set_title('编程语言流行度横向条形图', fontsize=14)
ax.invert_yaxis()  # 让流行度最高的语言显示在顶部

# 显示图表
plt.tight_layout()
plt.show()


'''------------------------------------------------------'''

# 示例数据
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
popularity = [85, 70, 60, 55, 45]

# 创建画布和轴对象
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向条形图
ax.barh(languages, popularity, color='lightgreen')



# 设置网格线（与刻度对齐，自然变密集）
ax.grid

# 其他样式设置
ax.set_xlabel('流行度', fontsize=12)
ax.set_ylabel('编程语言', fontsize=12)
ax.set_title('密集网格线的横向条形图', fontsize=14)
# ax.invert_yaxis()  # 按流行度降序排列

plt.tight_layout()
plt.show()

'''-------------------------------------------------------'''

# 示例数据
x = np.arange(1, 11)  # x轴数据
y = np.random.randint(10, 100, size=10)  # 随机y值

# 创建图形和轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制示例图形（散点图）
ax.scatter(x, y, color='red', s=50)

# 核心：调整x轴和y轴的刻度间隔（控制网格密度）
# x轴：从1到10，每0.5个单位一个刻度（更密集）
ax.set_xticks(np.arange(1, 10.1, 0.5))
# y轴：从0到100，每5个单位一个刻度（更密集）
ax.set_yticks(np.arange(0, 101, 5))

# 设置网格线（同时显示x和y轴网格）
ax.grid(
    axis='both',       # 同时对x轴和y轴生效
    linestyle='--',    # 虚线样式
    color='gray',      # 灰色网格
    alpha=0.7,         # 半透明
    linewidth=0.6      # 细线
)

# 其他设置
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)
ax.set_title('x轴和y轴均有密集网格线的图表', fontsize=14)

plt.tight_layout()
plt.show()
