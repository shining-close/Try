"""
14 - Draw an octagon that uses a different colour 
(randomly selected from a list of six possible colours) for each line. 
"""

import turtle
import random

colour = (["Blue", "Black", "Green", "Purple", "Red", "Orange"])

def turtleFunction1():
    turtle.shape("turtle")

    for i in range(0, 8):  # 代表画出几条边
        turtle.color(colour[random.randint(0, 5)]) # 每个边随机取一个颜色
        turtle.begin_fill()
        turtle.forward(100)  # 代表边的长度
        turtle.right(45)  # 代表角度：360/8=45

    turtle.exitonclick()

turtleFunction1()