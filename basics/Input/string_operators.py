lives = int (input("Please enter the number of lives."))

energy = int(input(" Please enter the energy level."))

sheild = int (input("Please enter the shield level."))

print()
print("Health has been set.")
print()

diamond = chr(4)
heart = chr(3)
hearts = lives * heart
energy = energy * diamond 
shield = sheild * diamond 

print(" Lives:", hearts)
print(" Energy", energy)
print(" Shield: ",shield)
