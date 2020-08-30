import turtle
t = turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
sides = int(turtle.numinput("Number of sides" , "How many sides in your spiral ?(1-15) " , 4))
colors = ["red","blue","green","yellow","orange","white","brown","pink","grey","magenta","purple","light green","sky blue","gold","magenta","indigo"]
for m in range (5,75) :
    t.left(360/sides + 5)
    t.width(m/25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0) :
        for n in range (sides) :
            t.pencolor (colors[n % sides])
            t.circle(m/3)
            t.left(350/sides)
    else :
        for n in range (sides) :
            t.pencolor (colors[n % sides])
            t.forward(m)
            t.right(350/sides)
