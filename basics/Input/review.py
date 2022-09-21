print("Hi I'm Ollie the Owl")
print("  _____  ")
print(" |o v o| ")
print("/|_---_|\ ")
name = input("Whats your name?")
print(f"Nice to meet you {name}")
Age = int( input("How old are you?"))
if Age < 18:
    guess = int( input("As you're under 18 you must guess the password to keep playing"))
else: 
    guess = 14
if guess != 14:
    print("Sorry you were wrong try again next time")
else:
    response1 = input("Do you want to be my friend?(yes or no)")

    while response1 != "yes":
        print("   _____  ")
        print("  |- v -| ")
        print(" /|_---_|\ ")
        response1 = input("You were meant to say yes")
    print("Yay I have a friend!!")
    print("   _____  ")
    print('"\|o v o|/"')
    print(" /|_---_|\ ")
