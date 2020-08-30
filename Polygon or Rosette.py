import turtle
t = turtle.Pen()
turtle.bgcolor ("blue")
t.speed(0)
t.width(4)
# Ask the user for the number of sides or circle
number = int(turtle.numinput("Number of sides or circles", "How many sides or circles in your shape ? "))
# Ask the user whether they want a rossete or a polygon
shape = turtle.textinput("Which shape do you want ? " , "Enter 'p' for polygon or 'r' for rosette: ")
for x in range(number) :
    if shape == 'r' :
        t.pencolor("light green")
        t.circle(100)
    else :
        t.pencolor("pink")
        t.forward(150)
    t.left(360/number)
