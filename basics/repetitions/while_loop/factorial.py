number = int(input("Please enter a number?"))
factorial = 1
while number > 0:
    factorial = number * factorial
    number -= 1
print(f"The factorial is {factorial}")