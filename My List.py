mylist = []
n = int(input("How many no. of friends name you want to enter : "))

print("\n")
for i in range(0, n):
    print("Enter name of your friend ", i+1, ":")
    item = input()
    mylist.append(item)
print("My friend list is ", mylist)

name =input ("What is your name ? ")
if name in mylist :
    print ("Welcome ! How are you ? I am Harshita`s python programme. Thanks for running this programme.")
else:
    print ("Sorry, I don't know you")

	
	
