import random
import turtle
t = turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
t.width(4)
number = int(turtle.numinput("Number of sides or circles", "How many sides or circles in your shape ? (1-15) "))
shape = turtle.textinput("Which shape do you want ? " , "Enter 'p' for polygon or 'r' for rosette: ")
colors = ["red","sky blue","green","yellow","orange","white","brown","pink","grey","purple","light green","sky blue","gold","magenta","indigo"]
for x in range(number) :
    if shape == 'r' :
        t.pencolor(random.choice(colors))
        t.circle(100)
    else :
        t.pencolor(random.choice(colors))
        t.forward(100)
    t.left(360/number)

