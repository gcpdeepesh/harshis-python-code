import random
import turtle
t = turtle.Pen()
turtle.bgcolor ("blue")
t.speed(0)
for n in range (200) :
    size = random.randint(10,70)
    x = random.randrange(-turtle.window_width()//3,
                         turtle.window_width()//3)
    y = random.randrange(-turtle.window_height()//3,
                        turtle.window_height()//3)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range (size) :
        t.pencolor("pink")
        t.forward(m*2)
        t.right(200)
