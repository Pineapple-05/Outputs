First_number = int(input("Please enter the first whole number."))
Second_number = int(input("Please enter the second whole number."))
Third_number = int(input("Please enter the third whole number."))
odd_numbers = 0
even_numbers = 0
if First_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1
if Second_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1
if Third_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1

print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")