import turtle
t = turtle.Pen()
t.speed(0)
t.width(2)
t.penup()
turtle.bgcolor("black")
sides = int (turtle.numinput("Number of sides", "How many sides in your rossete spiral?(2-6)"))
colors = ["orange","green","blue","yellow","pink","white"]
# Our outer spiral loop
for m in range(100) :
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    print(position,heading)
    t.width(m/20)
    # Our inner spiral loop
    for n in range(int(m/2)) :
        t.pendown()
        t.pencolor(colors[n%sides])
        t.circle(m/5)
        t.right(360/sides)
        t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.left(360/sides + 2)
