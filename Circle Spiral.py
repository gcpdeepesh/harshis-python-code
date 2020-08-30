import turtle
t=turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
t.width(3)
colors=["sky blue","yellow","light green","blue","orange","pink","white","purple","gold","magenta","red","brown"]

# Ask the user`s name using turtle`s tentinput pop up window.
sides = int(turtle.numinput("Number of circles",
                            "How many circles do you want(1-12)?"))

for x in range(200):
    t.pencolor(colors[x % sides])
    t.circle(x)
    t.left(960 / sides + 1)
    
