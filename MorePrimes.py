import math

import sympy

o=2
p=5

while(p<7000):
    if (sympy.isprime(p) == True):
        while(sympy.isprime(p+o) != True):
            o=o+2
        if (sympy.isprime(p+o) == True):
            a=p
            t=o
            b=a+t
            q=a*a
            y=b*b
            n=y-q


            PrimeCount=0
            i=2
            r=1
            z=0
            k=0
            u=0



            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r=r*((i-1)/i)
                    PrimeCount=PrimeCount+1
                i=i+1

            u=n/(round(n*r-0))


            while (q<(y-1)):
                if (sympy.isprime(q)==True):
                    z=z+1
                q=q+1

            while(u!=n/z):
                k=k+1
                u=n/(round(n*r-k))
            print("Between:",p,"and:",p+o,"subtraction value:",k)
    p=p+o
    o=2


