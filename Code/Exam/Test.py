import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 构造数据
data = {
    'Date': ['2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', 
             '2023-08-01', '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01'],
    'Total': [1000, 1500, 1750, 2000, 2250, 2500, 2750, 2500, 2700]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# 提取月份和年份，准备分两行显示
df['Month'] = df['Date'].dt.strftime('%b')  # 月份缩写（如Apr）
df['Year'] = df['Date'].dt.strftime('%Y')   # 年份（如2023）
# 组合成带换行符的标签（月份在上，年份在下）
df['Month_Year'] = df['Month'] + '\n' + df['Year']

# 设置图表
# plt.rcParams['figure.dpi'] = 300
# plt.figure(figsize=(10, 6))

# 绘制折线图
plt.plot(df['Month_Year'], df['Total'], color='tab:blue', linewidth=2, marker='o', markersize=6)

# 设置Y轴范围和刻度
plt.ylim(750, 2750)
plt.yticks(np.arange(1000, 2800, 250))

# 设置标签和标题
plt.xlabel('Month and Year', fontsize=10)
plt.ylabel('Total Sales', fontsize=10)
plt.title('Total Sales Over Time', fontsize=12)

# 调整x轴标签字体大小，避免拥挤
plt.xticks(fontsize=9)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 优化布局
plt.tight_layout()

plt.show()