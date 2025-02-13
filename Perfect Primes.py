import sympy
import math

x = 1
i = 1
z = 0

while (True):
    x = x*2+1
    if (sympy.isprime(z) == True):
        if (sympy.isprime(i+1) == True):
            z = z+1
            if (sympy.isprime(x) == True):
                print(i, ".", x, "times", 2**(round(math.log2(x))-1),
                      "is the perfect number:", x * 2**(round(math.log2(x))-1))
    i = i+1
