'''
练习2-创建一个简单的数学测验，询问用户的姓名，然后生成两个随机问题。
将他们的姓名、所问问题、答案和最终分数存储在.csv文件中。每当程序运行时,
它都应该添加到csv文件中, 而不是覆盖任何内容。
'''

import csv
import random

score = 0
name = input("What is your name: ")

q1_num1 = random.randint(10, 50)
q1_num2 = random.randint(10, 50)
question1 = str(q1_num1) + "+" + str(q1_num2) + " = "
ans1 = int(input(question1))
realans1 = q1_num1 + q1_num2
if ans1 == realans1:
    score = score + 1

q2_num1 = random.randint(10, 50)
q2_num2 = random.randint(10, 50)
question2 = str(q2_num1) + " + " + str(q2_num2) + " = "  # 修正原代码中q1_num1的笔误
ans2 = int(input(question2))
realans2 = q2_num1 + q2_num2
if ans2 == realans2:
    score = score + 1

file = open("QuizScore.csv", "a")
newrecord = name + "," + question1 + "," + str(ans1) + "," + question2 + "," + str(ans2) + "," + str(score) + "\n"
file.write(newrecord)
file.close()

