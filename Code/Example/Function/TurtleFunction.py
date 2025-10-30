import turtle


def turtleFunction1():
    turtle.shape("turtle")

    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(72)

    turtle.exitonclick()


def turtleFunction2():

    for i in range(0, 10):
        turtle.right(36)
        for i in range(0, 5):
            turtle.forward(100)
            turtle.right(72)
    turtle.exitonclick()

#turtleFunction1()
turtleFunction2()