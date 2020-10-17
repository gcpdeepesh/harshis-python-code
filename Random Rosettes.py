import random
import turtle
t = turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
for n in range (200) :
    size = random.randint(10,12)
    x = random.randrange(-turtle.window_width()//3,
                         turtle.window_width()//3)
    y = random.randrange(-turtle.window_height()//3,
                        turtle.window_height()//3)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range (size) :
        t.pencolor("pink")
        t.circle(55)
        t.pencolor("yellow")
        t.circle(50)
        t.pencolor("white")
        t.circle(45)
        t.pencolor("orange")
        t.circle(40)
        t.pencolor("blue")
        t.circle(35)
        t.pencolor("light green")
        t.circle(30)
        t.pencolor("gold")
        t.circle(25)
        t.pencolor("purple")
        t.circle(20)
        t.pencolor("grey")
        t.circle(15)
        t.left(200)
