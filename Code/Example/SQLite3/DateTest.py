import sqlite3
from datetime import datetime

# 连接数据库（不存在则自动创建）
conn = sqlite3.connect('events.db')
cursor = conn.cursor()

# 创建包含日期字段的表
# 使用TEXT类型存储ISO格式日期
cursor.execute('''
CREATE TABLE IF NOT EXISTS Events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT,  -- 存储格式如 '2023-10-05'
    created_at TEXT DEFAULT CURRENT_DATE  -- 默认为当前日期
)
''')

# 插入包含日期的数据示例
# 1. 插入指定日期
cursor.execute('''
INSERT INTO Events (event_name, event_date)
VALUES (?, ?)
''', ('技术会议', '2023-11-15'))

# 2. 插入当前日期（使用Python的datetime生成）
current_date = datetime.now().strftime('%Y-%m-%d')
cursor.execute('''
INSERT INTO Events (event_name, event_date)
VALUES (?, ?)
''', ('团队聚餐', current_date))

# 提交事务并关闭连接
conn.commit()
conn.close()

print("包含日期字段的表创建成功，并插入了示例数据")