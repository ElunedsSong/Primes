import math

import sympy

o=2
p=5
pc=2
r=1/6
i=5

while(p<7000000):
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


            PrimeCount=0
            z=0
            k=-50
            u=0


            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r=r*((i-2)/i)
                    PrimeCount=PrimeCount+1
                i=i+1
  
            u=n/(round(n*r))


            while (q<(y-1)):
                if (sympy.isprime(q)==True):
                    q=q+2
                    if(sympy.isprime(q)==True):
                        z=z+1
                    q=q-2    
                q=q+1

            while(u!=n/z):
                k=k+1
                u=n/(round(n*r-k))
            if(round(n/n*r != 0)):
                if((round(n*r)-round(.075*o*pc)) != 0):
                    if(n/(round(n*r)-round(.075*o*pc)) != 0):
                        print("From ",a,"To",b)
                        print("P-Min Twin-Primes:",(n/(n/(round(n*r)-round(0.04474*o*pc)))),"Actual Number Of Twin-Primes:",z,"P-Max Twin-Primes:",(n/(n/(round(n*r)-round(0.00122*o*pc)))))
                        if((n/(n/(round(n*r)-round(0.04474*o*pc))))>z):
                            print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    p=p+o
    o=2
