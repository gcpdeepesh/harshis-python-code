health = input("How is your health ? Are you feeling well ? (y-n): ").lower()
cold = input ("Are you having cold ? (y/n): ").lower()
fever = input ("Are you having fever ? (y/n): ").lower()
if (fever == 'n' and cold == 'y' and health == 'n'):
    print("You should carry a handkerchief with you and take medicines")
elif (fever == 'y' and cold == 'n' and health == 'y'):
    print("Please stay away from others")
elif (fever == 'y' and cold == 'y' and health == 'n'):
    print("I don`t think you should go out please stay at home")
elif (fever == 'n' and cold == 'n' and health == 'y'):
    print("You are perfectly alright")
elif (fever == 'y' and cold == 'y' and health == 'y'):
    print("I think you should take medicines")
elif (fever == 'n' and cold == 'n' and health == 'n'):
    print("You go and sleep")
elif (fever == 'n' and cold == 'y' and health == 'y'):
    print("Please carry a handkerchief")
elif (fever == 'y' and cold == 'n' and health == 'n'):
    print("Please take medicines and a sleep")
