import turtle
t = turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
sides = int(turtle.numinput("Number of sides" , "How many sides in your spiral ?(1-16) "))
colors = ["red","royal blue","light green","yellow","orange","white","pink","sky blue","purple","light green","sky blue","gold","magenta","black","indigo"]
for m in range (700) :
    t.pencolor(colors[m % sides])
    t.circle(50)
    t.forward(m/3)
    t.right(6000)
