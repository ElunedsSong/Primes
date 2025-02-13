import math
import sympy


x = 91+2*3*2*2
z = 0
if (sympy.isprime(x) == True):
    print(x, "is prime")
    z = 1
if (z == 0):
    print(x, "is not prime")

print(x)
