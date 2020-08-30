import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors=["sky blue","red","yellow","gray","light blue","white","magenta","orange","pink","brown","light green"]
your_name=turtle.textinput("Enter your name", "What is your name? ")
sides=int(turtle.numinput("Number of sides","Enter number of sides between 1-10."))
for x in range(100) :
    t.pencolor(colors[x%sides%11])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font=("Elgerian", int( (x*2 + 4) / 4), "bold"))
    t.left(360/sides+2)
