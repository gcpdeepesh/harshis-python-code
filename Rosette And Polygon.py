import turtle
t = turtle.Pen()
turtle.bgcolor ("red")
t.speed(0)
sides = int(turtle.numinput("Number of sides" , "How many sides in your spiral ? " , 5))
for m in range (5,75) :
    t.left(360/sides + 5)
    t.width(m/25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0) :
        for n in range (sides) :
            t.pencolor("yellow")
            t.circle(m/3)
            t.left(360/sides)
    else :
        for n in range (sides) :
            t.pencolor("blue")
            t.forward(m)
            t.right(360/sides)
