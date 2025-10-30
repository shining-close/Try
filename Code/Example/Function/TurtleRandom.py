import random
import turtle  # 导入turtle和random库
t = turtle.Turtle()  # 创建海龟笔t
# 创建一个常用颜色列表用来随机抽取颜色
colors = ["red", "orange", "lime", "yellow", "blue", "indigo", "purple", "black", "pink", "cyan", "green"]
t.speed(0)  # 速度范围0-10 小于0.5或大于10默认为0
# 界面顶端画五颜六色的云层
t.penup()  # 抬笔
t.goto(-765, 400)  # 随机跳到一个点
t.right(90)  # 笔向右旋转90度
t.pendown()  # 落笔
for k in range(26):  # 画26个半圆
    t.color(colors[random.randint(0, 10)])  # 每个半圆随机取一个颜色
    t.begin_fill()  # 开始填充颜色
    t.circle(30, 180)  # 半径为30，旋转180度
    t.left(180)  # 笔向左旋转180度
    t.end_fill()  # 结束填充颜色
for i in range(100):  # 烟花个数
    t.penup()  # 抬笔
    t.color(colors[random.randint(0, 10)])  # 每个烟花随机取一个颜色
    x = random.randint(-760, 750)  # 随机取横坐标
    y = random.randint(-400, 321)  # 随机取纵坐标
    t.goto(x, y)  # 随机跳到一个点
    t.pendown()  # 落笔
    for j in range(18):  # 画烟花
        t.left(10)
        t.forward(49)  # 往前走50
        t.left(180)
        t.forward(49)
        t.right(175)
        t.forward(49)
        t.left(180)
        t.forward(49)
        t.right(175)
t.hideturtle()  # 隐藏画笔箭头
turtle.done()  # 保持窗口打开，直到用户关闭它


"""
4、对turtle库和random库进一步了解如下：
(1)turtle库了解

# 导入库 import turtle

# 创建画布 window = turtle.Screen()

# 创建画笔 pen = turtle.Turtle()

# 前进 pen.forward(100)

# 后退 pen.backward(100)

# 左转 pen.left(90)

# 右转 pen.right(90)

# 绘制圆形 pen.circle(50)

# 抬起画笔 pen.penup()

# 移动到指定位置 pen.goto(100, 100)

# 开始填充颜色 pen.begin_fill()

# 落下画笔 pen.pendown()

# 结束填充颜色 pen.end_fill()

# 清空画布 pen.clear()

# 关闭画布 window.bye()

# 设置画笔颜色 pen.color("red")

# 设置画笔粗细 pen.width(2)

# 隐藏画笔箭头 pen.hideturtle()

# 保持窗口打开直到用户自己关闭 turtle.done()

# 显示绘制结果 window.mainloop()

(2)random库了解

# 导入库 import random

# 生成1到100之间的随机整数 random_number = random.randint(1, 100)

# 生成1.0到10.0之间的随机浮点数 random_float = random.uniform(1.0, 10.0)

创建一个列表：my_list = [1, 2, 3, 4, 5]

# 从列表中随机选择一个元素 random_element = random.choice(my_list)

# 打乱列表中元素的顺序 random.shuffle(my_list)

# 设置随机种子为42： random.seed(42)

random_number = random.randint(1, 100)

# 得到相同的随机数，因为种子相同 print(random_number)

"""