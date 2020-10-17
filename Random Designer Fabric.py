import random
import turtle
t = turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
colors = ["red","royal blue","light green","yellow","orange","white","pink","sky blue","purple","grey","brown","magenta","gold","indigo","maroon","blue","green","silver"]
for n in range (100) :
    # Generate spirals of random sizes/colors at ramdom locations.
    t.pencolor(random.choice(colors))        # Pick a random color
    size = random.randint(10,70)             # PIck a random spiral size
    # Generate a random (x,y) location on the screen
    size = random.randint(10,15)
    x = random.randrange(-turtle.window_width()//3,
                         turtle.window_width()//3)
    y = random.randrange(-turtle.window_height()//3,
                        turtle.window_height()//3)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range (size) :
        t.circle(30)
        t.forward(x/3)
        t.right(600)

       
