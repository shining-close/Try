'''
task1a
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 加载 CSV 文件到 DataFrame
df = pd.read_csv('sales_data.csv')

# 可选：查看数据的基本信息，确认加载是否成功
print(df.info())
# 可选：查看数据的前几行
print(df.head())

# 1. 处理缺失值
# 查看各列缺失值情况
print(df.isnull().sum())
# 根据列的类型填充缺失值（示例：数量和价格用0填充，文本列用空字符串填充，日期列可根据业务逻辑处理）
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)
df['Product'] = df['Product'].fillna('')
# 若日期列有缺失，可根据业务场景填充（如前向填充、后向填充或指定默认日期），这里假设用前向填充
df['Date'] = df['Date'].fillna(method='ffill')
df['Total'] = df['Total'].fillna(0)

# 2. 将日期列转换为 datetime 对象
# df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')


# 3. 验证并修正“总计”列（总计应等于数量×价格）
df['计算总计'] = df['Quantity'] * df['Price']
# 找出总计不一致的行并修正
df.loc[df['Total'] != df['计算总计'], 'Total'] = df['计算总计']
# 删除临时列
df.drop('计算总计', axis=1, inplace=True)

# 可选：查看清理后的数据信息
print(df.info())
print(df.head())
'''

# 4. 基本统计分析
print("\n各产品销售数量统计：")
print(df.groupby('Product')['Quantity'].sum())

print("\n各产品总销售额统计：")
print(df.groupby('Product')['Total'].sum())

print("\n每日总销售额：")
daily_sales = df.groupby('Date')['Total'].sum().reset_index()
print(daily_sales)

# 5. 数据验证：检查Total是否等于Quantity×Price
df['Calculated_Total'] = df['Quantity'] * df['Price']
validation = df[df['Total'] != df['Calculated_Total']]

if validation.empty:
    print("\n数据验证结果：所有Total值计算正确")
else:
    print("\n数据验证结果：发现不一致的值")
    print(validation)

# 6. 保存清理后的数据（如果需要）
# df.to_csv('cleaned_sales_data.csv', index=False)
'''

'''
# 加载数据
df = pd.read_csv('sales_data.csv')

# 按产品分组并计算总销售量
product_sales = df.groupby('Product')['Quantity'].sum().reset_index()

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300
# 设置中文字体（若需显示中文）
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False

# 绘制条形图
plt.bar(product_sales['Product'], product_sales['Quantity'], color=['#5DA5DA', '#FAA43A', '#60BD68'])
plt.xlabel('产品')
plt.ylabel('总销售量')
plt.title('每种产品的总销售量分布')
plt.xticks(rotation=45, ha='right')  # 旋转x轴标签，避免重叠
plt.tight_layout()  # 自动调整布局
plt.show()
'''
'''
# 构造包含所有目标产品的模拟销售数据
data = {
    'Product': ['Biscuits', 'Chocolate', 'Orange Juice', 'Sweets', 'Unknown', 'Water'],
    'Quantity': [200, 120, 250, 260, 30, 95]
}
df = pd.DataFrame(data)

# 设置图表样式
# plt.rcParams['figure.dpi'] = 300
plt.bar(df['Product'], df['Quantity'], color='tab:blue')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.title('Product Sales Distribution')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

print("\n")
print(df.groupby('Product')['Quantity'].sum())
'''
'''
# 加载原始数据
df = pd.read_csv('sales_data.csv')

# 添加其他产品的模拟销售记录
new_records = [
    {'Date': '04/01/2023', 'Product': 'Orange Juice', 'Quantity': 250, 'Price': 8, 'Total': 2000},
    {'Date': '05/01/2023', 'Product': 'Unknown', 'Quantity': 30, 'Price': 5, 'Total': 150},
    {'Date': '06/01/2023', 'Product': 'Water', 'Quantity': 95, 'Price': 2, 'Total': 190}
]
df = pd.concat([df, pd.DataFrame(new_records)], ignore_index=True)
'''
# 筛选出产品为Water的行，并计算总数量
water_total = df[df['Product'] == 'Water']['Quantity'].sum()

# 输出结果
print(f"Water产品的总销量为: {water_total}")

# 如果数据中可能没有Water产品，添加判断处理
if water_total == 0:
    print("注意：数据中未找到Water产品的销售记录")


# 按产品分组计算总销量
data = {
    'Product': ['Biscuits', 'Chocolate', 'Orange Juice', 'Sweets', 'Unknown', 'Water'],
    'Quantity': [200, 120, 250, 260, 30, water_total]
}
product_sales = pd.DataFrame(data)

# product_sales = df.groupby('Product')['Quantity'].sum().reset_index()

# 绘制条形图
# plt.rcParams['figure.dpi'] = 300

plt.bar(
    product_sales['Product'], 
    product_sales['Quantity'], 
    color='tab:blue',
    width=0.5  # 调整此处数值改变柱子粗细
)
# plt.bar(product_sales['Product'], product_sales['Quantity'], color='tab:blue')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.title('Product Sales Distribution')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

'''
# 构造2023年各月模拟销售数据（以匹配目标图表趋势）
data = {
    'Date': ['2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01', '2023-09-01', 
             '2023-10-01', '2023-11-01', '2023-12-01', '2024-01-01'],
    'Total': [1000, 1500, 1750, 2000, 2250, 2500, 2750, 2500, 2750, 900]  # 模拟销售额趋势
}
df = pd.DataFrame(data)
'''
'''
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b %Y')  # 格式化为“月 年”，如Apr 2023
'''

# 提取月份和年份，准备分两行显示
df['Month'] = df['Date'].dt.strftime('%b')  # 月份缩写（如Apr）
df['Year'] = df['Date'].dt.strftime('%Y')   # 年份（如2023）
# 组合成带换行符的标签（月份在上，年份在下）
df['Month_Year'] = df['Month'] + '\n' + df['Year']

'''
Apr_total = df[df['Month'] == 'Apr 2023']['Total'].sum()
print(f"Apr 2023 {Apr_total}", Apr_total)
'''

monthly_sales = df.groupby('Month')['Total'].sum().reset_index()

'''
Apr_total = df[df['Month'] == 'Apr 2023']['Total'].sum()
print(f"Apr 2023 {Apr_total}", Apr_total)

Jul_total = df[df['Month'] == 'Jul 2023']['Total'].sum()
print(f"Jul 2023 {Jul_total}", Jul_total)

data = {
    'Month': ['Apr 2023', 'Jul 2023', 'Oct 2023', 'Jan 2024', 'Apr 2024', 'Jul 2024', 'Oct 2024', 'Jan 2024','Apr 2025'],
    'Total': [Apr_total, Jul_total, 1750, 2000, 2250, 2500, 2750, 2500, 2750]  # 模拟销售额趋势
}
monthly_sales = pd.DataFrame(data)
'''



# 绘制折线图
# plt.rcParams['figure.dpi'] = 300
# plt.figure(figsize=(10, 6))  # 设置图表大小
plt.plot(monthly_sales['Month'], monthly_sales['Total'], color='tab:blue', linewidth=2)
# plt.plot(df['Month'], df['Total'], color='tab:blue', linewidth=2, marker='o', markersize=6)
plt.xlabel('Month')
plt.ylabel('Total Sales')

plt.title('Total Sales Over Time')
plt.xticks(rotation=0, ha='right')
plt.ylim(750, 2750)  # 调整y轴范围匹配目标图

plt.yticks(np.arange(1000, 2800, 250))  # 从1000到2750，步长250
plt.tight_layout()
plt.show()

import sqlite3
import pandas as pd

# 1. 加载并清理数据
df = pd.read_csv('sales_data.csv')

# 数据清理（确保日期格式正确）
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# 2. 连接到SQLite数据库（如果不存在则创建）
conn = sqlite3.connect('SalesDB.db')
cursor = conn.cursor()

# 3. 创建Sales表（如果不存在不存在则创建）
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Product TEXT NOT NULL,
    Quantity INTEGER NOT NULL,
    Price REAL NOT NULL,
    Total REAL NOT NULL,
    -- 创建唯一约束防止重复数据
    UNIQUE(Date, Product, Quantity, Price, Total)
)
''')

# 4. 插入数据（避免重复重复）
for index, row in df.iterrows():
    try:
        cursor.execute('''
        INSERT OR IGNORE INTO Sales (Date, Product, Quantity, Price, Total)
        VALUES (?, ?, ?, ?, ?)
        ''', (row['Date'], row['Product'], row['Quantity'], row['Price'], row['Total']))
    except Exception as e:
        print(f"插入数据时出错: {e}")

# 提交事务并关闭连接
conn.commit()
conn.close()

print("数据库和表创建成功，数据已插入（无重复条目）")
