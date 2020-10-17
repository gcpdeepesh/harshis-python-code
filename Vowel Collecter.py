letter = (input("Please enter a word to know the vowels : ")) .lower()
txt = letter
vowels = ('a','e','i','o','u')
if letter in vowels :
    x = txt.split()
    print(letter, "has" ,x)
else :
    print("Sorry, there is no vowel")
    
