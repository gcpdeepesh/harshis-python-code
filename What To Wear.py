rainy = input("How`s the weather outside ? Is it raining (y/n):").lower()
cold = input ("Is it cold outside ? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):
    print("Is it important, if yes you`d better wear a raincoat otherwise I wil suggest you to stay at home.")
elif (rainy == 'y' and cold == 'n'):
    print("Don`t forget to carry an umbrella with you.")
elif (rainy == 'n' and cold == 'y'):
    print("Put on your jacket it`s cold out!")
elif (rainy == 'n' and cold == 'n'):
    print("Wear whateever you want, it`s beautiful outside!")
