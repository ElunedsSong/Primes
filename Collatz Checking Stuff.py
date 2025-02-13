import math

x = 5
z = 1

while (x < 100):
    while (z == 1):
        x = x*2
        if (x % 18 == 4):
            z = 0
        if (x % 18 == 16):
            z = 0
    x = x-1
    x = x/3
    print(x)
    z = 1

x = 1

while (x < 100):
    if (x % 3 != 0):
        print(x)
    x = x+2
