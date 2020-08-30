#def writetable(xx):
#     for x in range (10) :
#		y=(x + 1)*xx
#		print(str(xx) + " x " + str (x+1)+ " = " + str(y))

def writetable():
	xx = eval(input("Whose table you want ? "))
	for x in range (10):
		y=(x + 1)*xx
		print(str(xx) + " x " + str (x+1)+ " = " + str(y))

writetable()