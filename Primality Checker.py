import math

import sympy
q=0
b=282
c=13
while(b>-1):
    q=q+(c**b)
    b=b-1

n=0

if (sympy.isprime(q)==True):
    n=1

if (n==1):    
    print(q,"is prime (Sympy)")
if (n==0):
    print(q,"is not prime (Sympy)")