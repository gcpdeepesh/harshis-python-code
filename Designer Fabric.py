import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
for x in range (200) :
    t.pencolor("blue")
    t.circle(100)
    t.forward(x/3)
    t.right(200)
