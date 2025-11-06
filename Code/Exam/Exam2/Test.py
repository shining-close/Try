## 任务 1a：数据加载与清洗

# 1. 加载并查看数据

import pandas as pd

# 加载数据
df = pd.read_csv('cyber_incidents.csv')
# 打印前5行和数据框形状
print('=== First 5 rows ===')
print(df.head())
print('=== DataFrame shape ===')
print(df.shape)

# 2. 转换日期列类型
# 转换Date列为datetime类型
df['Date'] = pd.to_datetime(df['Date'])
# 打印转换后的列类型
print('=== dtype of Date after conversion ===')
print(df['Date'].dtype)

# 3. 处理缺失值
# 检查缺失值数量
missing_before = df.isnull().sum().sum()
# 这里假设用0填充Count列的缺失值（根据场景合理填充）
df['Count'] = df['Count'].fillna(0)
missing_after = df.isnull().sum().sum()
print('=== Total missing values after handling Date: {} (from {} to {}) ==='.format(missing_after, missing_before, missing_after))

# 4. 标准化事件类型（大写并去空格）
# 转换Incident_Type为大写并去除空格
df['Incident_Type'] = df['Incident_Type'].str.upper().str.strip()
# 打印唯一的事件类型
print('=== Incident_Type values ===')
print(df['Incident_Type'].unique())


## 任务 1b：数据可视化

# 1. 按事件类型绘制柱状图

import matplotlib.pyplot as plt

# 按Incident_Type分组求和
incident_counts = df.groupby('Incident_Type')['Count'].sum()
# 绘制柱状图
incident_counts.plot(kind='bar', title='Total Incidents per Incident Type')
plt.xlabel('Incident Type')
plt.ylabel('Total Incidents')
plt.show()
# 打印各类型的总数
print('=== Total incidents per Incident Type ===')
print(incident_counts)

# 2 折线图
# （假设已完成前面的数据加载与清洗，df 是处理后的 DataFrame）

# 筛选2025年的数据
df_2025 = df[df['Date'].dt.year == 2025]

# 按月分组并计算每月事件总数
monthly_totals = df_2025.groupby(df_2025['Date'].dt.to_period('M'))['Count'].sum()
monthly_totals = monthly_totals.reset_index(name='Total Incidents')  # 重置索引并命名列

# 打印2025年每月的事件总数
print("=== Monthly totals for 2025 ===")
print(monthly_totals)

# 创建折线图
plt.figure(figsize=(10, 6))
plt.plot(monthly_totals['Date'].astype(str), monthly_totals['Total Incidents'], marker='o')
plt.title('Monthly Incident Totals (2025)')
plt.xlabel('Month (YYYY-MM)')
plt.ylabel('Total Incidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


## Python Task 2: Database Management and File Handling [15 Marks]

# 任务 2a：数据库创建与数据插入
import sqlite3
import pandas as pd

# 创建SQLite数据库
conn = sqlite3.connect('IncidentsDB.db')
cursor = conn.cursor()

# 创建Incidents表（带唯一约束）
create_table_query = """
CREATE TABLE IF NOT EXISTS Incidents (
    Date TEXT,
    System TEXT,
    Incident_Type TEXT,
    Count INTEGER,
    UNIQUE(Date, System, Incident_Type)
);
"""
cursor.execute(create_table_query)

# 插入清洗后的数据（假设df是Task1处理后的DataFrame）
# 先删除可能重复的记录（根据唯一约束）
df = df.drop_duplicates(subset=['Date', 'System', 'Incident_Type'])

# 将数据插入数据库
rows_inserted = df.to_sql('Incidents', conn, if_exists='append', index=False)
print(f"=== Rows inserted into Incidents table: {rows_inserted} ===")

conn.commit()

# 任务 2b：数据库查询
# 查询2025年总事件数
total_2025_query = """
SELECT SUM(Count) 
FROM Incidents 
WHERE strftime('%Y', Date) = '2025';
"""
total_2025 = cursor.execute(total_2025_query).fetchone()[0]
print(f"[2b-1] Total incidents in 2025: {total_2025}")

# 查询2025年事件数最高的三个系统
top_systems_query = """
SELECT System, SUM(Count) AS Total
FROM Incidents 
WHERE strftime('%Y', Date) = '2025'
GROUP BY System
ORDER BY Total DESC
LIMIT 3;
"""
top_systems = pd.read_sql(top_systems_query, conn)
print("[2b-2] Top 3 systems by incidents in 2025:")
for idx, row in top_systems.iterrows():
    print(f"- {row['System']}: {row['Total']}")


# 任务 2c：导出结果到 CSV
# 打印DataFrame
print("\n[2c] Top 3 systems DataFrame (to be saved to top3_systems.csv):")
print(top_systems)

# 保存到CSV
top_systems.to_csv('top3_systems.csv', index=False)

# 关闭数据库连接
conn.close()


## Python Task 3: Neural Network (PyTorch) [12 Marks]
# Task 3a: 模型设置（数据生成与随机种子控制）
import torch

# 1. 设置随机种子，确保结果可复现
torch.manual_seed(42)  # 固定随机种子，使每次运行生成的随机数相同

# 2. 生成合成特征X（200个样本，4个特征）
X = torch.randn(200, 4)  # 随机生成符合正态分布的特征数据

# 3. 生成二值目标标签y（0或1）
# 基于特征简单计算阈值，生成0/1标签（模拟高风险事件可能性）
y = (torch.sum(X, dim=1) > 0.5).float().view(-1, 1)  # 转换为float类型并调整形状为[200, 1]

# 4. 打印X和y的形状
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")


# Task 3b: 模型定义与初始化
import torch.nn as nn
import torch.optim as optim

# 1. 定义神经网络类RiskNN
class RiskNN(nn.Module):
    def __init__(self):
        super(RiskNN, self).__init__()
        # 输入层→隐藏层：4→8，使用ReLU激活
        self.hidden = nn.Linear(in_features=4, out_features=8)
        self.relu = nn.ReLU()
        # 隐藏层→输出层：8→1，使用Sigmoid激活（输出0-1概率）
        self.output = nn.Linear(in_features=8, out_features=1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # 前向传播过程
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)
        x = self.sigmoid(x)
        return x

# 2. 实例化模型、定义损失函数和优化器
model = RiskNN()  # 实例化神经网络
criterion = nn.BCELoss()  # 二分类交叉熵损失（适合0-1标签）
optimizer = optim.SGD(model.parameters(), lr=0.05)  # SGD优化器，学习率0.05