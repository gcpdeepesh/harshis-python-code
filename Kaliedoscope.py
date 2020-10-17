import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.width(3)
colors = ["red","blue","light green","yellow","orange","purple","white","gold"]
for n in range (50) :
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_width()//2)
    # First spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range (size) :
        t.forward(m*2)
        t.left(50)
    # Second spiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range (size) :
        t.forward(m*2)
        t.left(50)
    # Third spiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range (size) :
        t.forward(m*2)
        t.left(50)
    # Fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range (size) :
        t.forward(m*2)
        t.left(50)
