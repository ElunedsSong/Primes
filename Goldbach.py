import math
import sympy

x = 10000000
r = 0
temp = 0
z = 3

while (x < 1000000000):
    while (r == 0):
        temp = z + 2 * (x-z)
        if (sympy.isprime(temp) == True):
            if (z > 1000):
                print("for", x, z, "and", temp, "is correct")
            r = 1
        z = z+2
        while (sympy.isprime(z) != True):
            z = z+2
    r = 0
    z = 3
    x = x+2
    if (x % 10000000 == 0):
        print(x)
