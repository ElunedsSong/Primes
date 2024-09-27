import math

import sympy

w=0
i=0
FPrime=2
FRPrime=1
p=3
Track=1
F1Prime=0
F2Prime=0
FPrimeStorage=0
u=0

while(w==0):
    while(Track<10):
        while(sympy.isprime(p) != True):
             p=p+2
        if (sympy.isprime(p) == True):
            FPrime=FPrime*p
            Track=Track+1
            p=p+2
    p=p+2
    while(FRPrime<FPrime):
        while(sympy.isprime(p) != True):
            p=p+2
        if (sympy.isprime(p) == True):
            FRPrime=FRPrime*p
            p=p+2
    FRPrime = FRPrime / (p-2)


    FPrimeStorage = FPrime
    while(FPrimeStorage>FRPrime):    
        FPrimeStorage = FPrimeStorage-FRPrime

    if (FPrimeStorage < (FPrime-FRPrime)):
        if (sympy.isprime(FPrimeStorage) == True):    
            print(FPrime-1, "is prime, probably")
            print(FPrime+1, "is prime, probably")

    Track=Track+1
    if(Track==10):
        w=1
        print(FPrime)


        