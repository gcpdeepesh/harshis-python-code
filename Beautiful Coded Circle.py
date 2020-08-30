import turtle
t=turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
colors=["blue","orange","yellow","red"]
for x in range (200) :
	t.pencolor (colors[x % 4])
	t.circle(x)
	t.left (95)
