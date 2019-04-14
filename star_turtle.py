import turtle

phil = turtle.Turtle()

phil.getscreen().bgcolor("#42dcf4")

phil.penup()
phil.goto(-250,100)
phil.pendown()


def star(turtle, size):
    if size <= 10:
        return 
    else:
        for i in range(5):
            turtle.speed(10)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)

star(phil, 360)

turtle.done()
