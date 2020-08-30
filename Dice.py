import random
keep_going = True
while keep_going :
    # 'Roll' five random dice
    dice = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10) : # "Roll"
        dice[i] = random.randint(1,100)
    print("You rolled:", dice)
    answer = input("Hit [ENTER] to keep going ")
    keep_going = (answer == "")
