"""13 - Draw a circle."""

import turtle

t = turtle.Turtle()  # 创建海龟笔
                     # 如果不创建，就直接用turtle,pu()

#This function draw a circle in x,y of radius r
def drawCircle(x,y,r):
    t.pu()       # turtle.penup() 别名turtle.pu() 画笔抬起，不留下痕迹
    t.goto(x,y-r)# -r because we want xy as center and Turtles starts from border
                 # 从当前的点指向括号内所给坐标
    t.pd()       # turtle.pendown() 别名turtle.pd() 画笔落下，留下痕迹
    t.circle(r)
 
#draw a cicle in (50,30) with r=50
drawCircle(50,30,50)

drawCircle(20,30,50)

'''-----------------------------------------'''

def drawCircle(x,y,r):
    t.pu()
    t.goto(x-r,y)#-r because we want xy as center and Turtles starts from border
    t.pd()
    t.circle(r)
 
#draw a cicle in (50,30) with r=50
drawCircle(50,30,50)
 
#draw a cicle in (20,50) with r=100
drawCircle(20,50,100)

