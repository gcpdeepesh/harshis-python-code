driving_age = eval(input("What is the legal driving age in your area ? "))
your_age = eval(input("What is your age ? "))
if your_age >= driving_age :
    print ("You are old enough to drive legally")
if your_age < driving_age :
    print ("Sorry you can drive" , driving_age - your_age, "years later.")
