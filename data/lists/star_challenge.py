
'''
# ***
def prin():
    print("*",end="")



for i in range(3):
    prin()
'''


'''
***
***
***
'''
'''
for i in range(3):
    print()
    for a in range(3):
        prin()

'''
'''
*
**
***
****
'''
'''
b=0
for i in range(4):
    b += 1
    print()
    for a in range(b):
        prin()
'''
'''
* ***
** **
*** *

'''
b = 0
c = 4
for i in range(3):
    b += 1
    c -= 1
    print()
    for a in range(b):
        print("*",end="")
    print(" ", end="")
    for d in range(c):
        print("*",end="")

