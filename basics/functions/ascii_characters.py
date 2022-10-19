print("Program Started!")
code = int(input("Please enter an ASCII code:"))
if code in range(32, 127):
    letter = ord(code)
    print(f"The character represented by the ASCII code {code} is: {letter} ")
else:
    print("please restart programme choosing suitable number with in the range 32-126")
