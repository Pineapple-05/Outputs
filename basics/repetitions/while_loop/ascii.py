number = int(input("How many bars should be charged?"))
count = 0
bar = "|"
while count < number:
    count = count + 1
    bars = bar * count
    print("Charging: ", bars)



