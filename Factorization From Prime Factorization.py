import math

import sympy


i=3
u=5
o=2

factorizedsum =1

number=3
while(u<100000):
    number=number*u
    while(i<u+1):
        if (sympy.isprime(i) == True):
            factorizedsum= factorizedsum + number/i
            factorizedsum= factorizedsum + i
        i=i+2
    print("T-Factor of",number, "is",factorizedsum, "F-%:",factorizedsum/number)
    factorizedsum=1
    i=3
    o=2
    while(sympy.isprime(u+o) != True):
        o=o+2
    u=u+o
    
