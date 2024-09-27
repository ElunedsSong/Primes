import math

import sympy

o=2
p=13
r=1
i=13

v=5*7*11*6/5
z=3*5*8

while(p<v):
    if (sympy.isprime(p) == True):
        while(sympy.isprime(p+o) != True):
            o=o+2
        if (sympy.isprime(p+o) == True):
            a=p

            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r=r*((i-2)/i)
                i=i+1
            

    p=p+o
    o=2
print(r)
print(z*r)