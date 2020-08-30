import turtle
t = turtle.Pen()
t.speed(0)
t.width(2)
t.penup()
turtle.bgcolor("black")
# Ask the user for the number of sides to 4, min 2, max 6.
sides = int (turtle.numinput("Number of sides", "How many sides in your spiral of spirals? (2-6)",4,2,6))
colors = ["yellow","blue","orange","light green","pink","white"]
# Our outer spiral loop
for m in range(100):
    t.forward(m*4)
    position = t.position() # Remember this corner of the spiral
    heading = t.heading()   # Remember the direction we were heading
    print(position, heading)
    # Our "inner" spiral loop
    # Draws a little spiral at each corner of thebig spiral
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setpos(position)      # Go back to the big spiral`s x location
    t.setheading(heading)   # Point in the big spiral`s heading
    t.left(360/sides + 2)   # Aim at the next point on the big spiral     