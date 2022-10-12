name = input("My names Ollie, whats your name?")
if name == "Ollie" or name == "ollie":
    print("wow, we have the same name")
adventure = input(f"{name} would you want to go on an adventure with me? (yes/no)")
if adventure == "yes":
    ready = "0"
    Type = input("Great, should we go on a scary or safe adventure")
    if Type == "scary":
        ready = input("Ok, lets go on a scary adventure, are you ready? (yes/no)")
    elif Type == "safe":
        ready = input("To go the safe way we should go this way, are you ready? (yes/no) ")
    if ready == "yes":
        print("Woohooo let's go")
    elif ready == "no":
        print("That's fine you can catch me up later")
    else:
        print("Umm, Im not really sure what you mean")
else:
    print("oh, ok, that's fine")
    print("I'm not crying its just hayfever")


