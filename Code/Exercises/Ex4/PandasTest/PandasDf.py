'''
编写一个Pandas程序以获取给定DataFrame的前三行。
'''

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Paul', 'Kathe', 'Joseph', 'Linda', 'Michael', 'Matt', 'Laurentine', 'Chirstian', 'Jonas'],
             'score': [12.5, 10, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print("First three rows of the data frame:")
print(df.iloc[:3])

'''
编写一个 Pandas 程序来选择考试中尝试次数大于 2 的行。
'''

print("First three rows of the data frame:")
print(df[df['attempts'] > 2])

'''
编写一个Pandas程序来计算DataFrame的行数和列数。
'''

print("First three rows of the data frame:")
total_rows = len(df.axes[0])
total_cols = len(df.axes[1])
print("Number of Rows: " + str(total_rows))
print("Number of Columns: " + str(total_cols))

'''
编写一个Pandas程序以选择分数在14到20之间（包括14和20）的行
'''

print("Rows where score between 14 and 20 (inclusive):")
print(df[df['score'].between(14, 20)])

'''
编写一个Pandas程序，将行 'c' 的分数改为11.5
'''

print("\nOriginal data frame:")
print(df)
print("\nChange the score in row 'c' to 11.5:")
df.loc['c', 'score'] = 11.5
print(df)

'''
编写一个Pandas程序来计算DataFrame中每个不同学生的平均分
'''

print("\nMean score for each different student in data frame:")
print(df['score'].mean())