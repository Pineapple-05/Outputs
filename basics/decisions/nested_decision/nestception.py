location = input("Where should I look?")
if location == "in the bedroom" :
    location2 = input("Where in the bedroom should I look?")
    if location2 == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

if location == "in the bathroom" :
    location2 = input("Where in the bathroom should I look?")
    if location2 == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

if location == "in the lab" :
    location2 = input("Where in the lab should I look?")
    if location2 == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

if location != "in the lab" and location != "in the bedroom" and location != "in the bathroom":
    print("I do not know where that is but I will keep looking.")