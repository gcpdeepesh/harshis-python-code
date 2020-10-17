import turtle
t=turtle.Pen()
turtle.bgcolor ("black")
t.speed (0)
colors=["blue","green","yellow","orange"]
for x in range (200) :
	t.pencolor (colors[x % 4])
	t.circle(x)
	t.left (92)
