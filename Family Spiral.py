import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors=["sky blue","purple","white","brown","gold","gray","light green","blue","orange","yellow","red","magenta","green"]
family = []
name = turtle.textinput("My family","Enter a name, or just hit [ENTER] to end")
while name!= "":
    family.append(name)
    name = turtle.textinput("My family","Enter a name, or just hit [ENTER] to end" )
    
for x in range(200) :
        t.pencolor(colors[x%len(family)])
        t.penup()
        t.forward(x*4)
        t.pendown()
        t.write(family[x%len(family)], font = ("Elgerian", int((x+4)/4), "bold"))
        t.left(200/len(family) + 2)
