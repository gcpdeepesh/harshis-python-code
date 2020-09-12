import turtle
t=turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
colors=["pink","light green","blue","yellow","gold","magenta","white"]

# Ask the user`s name using turtle`s textinput pop up window
your_name = turtle.textinput("Enter your name", "What is your name?")

# Draw a spiral of the name on the screen, written 100 times
for x in range(360) :
    t.pencolor( colors[x % 7] )
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name, font = ("Elgerian", int((x + 4) / 4), "bold"))
    t.left (160)
