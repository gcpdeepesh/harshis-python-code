import turtle
t = turtle.Pen()
turtle.bgcolor ("blue")
t.speed(0)
sides = int(turtle.numinput("Number of sides" , "How many sides in your spiral ?(1-16) " , 5))
colors = ["red","sky blue","green","yellow","orange","white","brown","pink","grey","purple","light green","sky blue","gold","magenta","black","indigo"]
for m in range (5,100) :
    t.left(360/sides + 1)
    t.width(m/10+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0) :
        for n in range (sides) :
            t.pencolor (colors[n % sides])
            t.circle(m/3)
            t.left(360/sides)
    else :
        for n in range (sides) :
            t.pencolor (colors[n % sides])
            t.forward(m)
            t.right(360/sides)
