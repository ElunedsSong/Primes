import math

import sympy

w=0
lo=0
o=2
p=7
r=1/30
i=7
z=0

while(w==0):
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

            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r=r*((i-6)/i)
                i=i+1
            if (o==2):
                if(a>237329428):
                    z=0
                    print("Found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Prime: ",a)
                    while (q<(y-1)):
                        if (sympy.isprime(q)==True):
                            q=q+4
                            if(sympy.isprime(q)==True):
                                q=q+2
                                if(sympy.isprime(q)==True):
                                    q=q+4
                                    if(sympy.isprime(q)==True):
                                        q=q+2
                                        if(sympy.isprime(q)==True):
                                            q=q+4
                                            if(sympy.isprime(q)==True):
                                                z=z+1
                                            q=q-4
                                        q=q-2
                                    q=q-4
                                q=q-2
                            q=q-4
                        q=q+2
                    print("Number of 6 run primes actually in gap: ",z)
                    if (z==0):        
                        w=1
    p=p+o
    o=2