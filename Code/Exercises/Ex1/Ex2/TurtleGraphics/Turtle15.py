"""15 - Draw a pattern that will change each time the programme is run. 
Use random function to pick the number of lines, the length of each line and the angle of each turn."""
"""绘制一个每次程序运行时都会改变的图案。
使用随机函数来选择线的数量，每条线的长度和每个转弯的角度。"""

import turtle
import random

num_line = random.randint(0, 9)
len_line = random.randint(0, 100)
angle = random.randint(0, 360)

def turtleFunction1():
    turtle.shape("turtle")

    for i in range(0, num_line):  # 代表画出几条边
        
        turtle.forward(len_line)  # 代表边的长度
        turtle.right(angle)  # 代表角度：360/8=45

    turtle.exitonclick()

turtleFunction1()