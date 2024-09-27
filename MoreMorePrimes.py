import math

import sympy

o=2
p=5
pc=2
i=2
r=1

while(p<700000):
    if (sympy.isprime(p) == True):
        while(sympy.isprime(p+o) != True):
            o=o+2
        if (sympy.isprime(p+o) == True):
            pc=pc+1
            a=p
            t=o
            b=a+t
            q=a*a
            y=b*b
            n=y-q

            print("For ",a,"To ",b, "Which is a^2 ",q,"to b^2",y)


            z=0
            k=0

            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r=r*((i-1)/i)
                i=i+1


            while (q<(y-1)):
                if (sympy.isprime(q)==True):
                    z=z+1
                q=q+1
            if(round(n/n*r != 0)):
                if((n*r-round(.111111*o*pc)) != 0):
                    if(n/(round(n*r)-round(.11111*o*pc)) != 0):
                        print("P-Min Primes:",(n/(n/(round(n*r)-round(0.154*o*pc)))),"Actual Number Of Primes:",z,"P-Max Primes:",(n/(n/(round(n*r)-round(0.0679*o*pc)))))
    p=p+o
    o=2