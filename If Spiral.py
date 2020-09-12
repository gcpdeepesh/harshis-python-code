answer = input("Do you want to see a spiral? y/n:")
if answer == 'y' :
    print("Working...")
    import turtle
    t=turtle.Pen()
    turtle.bgcolor("blue")
    t.speed(0)
    t.width(2)
    for x in range(200):
        t.pencolor("yellow")
        t.forward(x*2)
        t.left(100)
    print("Okay we are done")
else :
    print("Don`t need any, no problem better luck next time")

        
 
