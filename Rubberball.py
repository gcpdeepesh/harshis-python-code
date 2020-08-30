import turtle
t=turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
sides=eval(input("Enter a number of sides between 1 and 14:"))
colors=["light blue","red","yellow","light green","purple","green","white","pink","brown","orange","grey","green","maroon","magenta"]
for x in range (360) :
	t.pencolor (colors[x % sides])
	t.forward(x * 3/sides + x)
	t.left(360/sides + 91)
	t.width(x * sides/100)
