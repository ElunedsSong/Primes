import math

import sympy

o=2
p=5
pc=2
r1=1/3
r2=1/6
r3=1/6
i=5
m=5

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

            k=-50
            z1=0
            z2=0
            z3=0

            m=i

            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r3=r3*((i-3)/i)
                i=i+1
            i=m

            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r1=r1*((i-1)/i)
                i=i+1
            i=m
            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r2=r2*((i-2)/i)
                i=i+1


            while (q<(y-1)):
                if (sympy.isprime(q)==True):
                    z1=z1+1
                    q=q+2
                    if(sympy.isprime(q)==True):
                        z2=z2+1
                        q=q+4
                        if(sympy.isprime(q)==True):
                            z3=z3+1
                        q=q-4
                    q=q-2    
                q=q+1



            if(round(n/n*r1 != 0)):
                if((n*r1-round(0.154*o*pc)) != 0):
                    if(n/(round(n*r1)-round(.154*o*pc)) != 0):
                        print("For ",a,"to",b,"r*n values:",r1*n,r2*n,r3*n)
                        print("P-Min Primes:",(n/(n/(round(n*r1)-round(0.154*o*pc)))),"Actual Number Of Primes:",z1,"P-Max Primes:",(n/(n/(round(n*r1)-round( 0.012*o*pc)))))
            if(round(n/n*r2 != 0)):
                if((round(n*r2)-round(.075*o*pc)) != 0):
                    if(n/(round(n*r2)-round(.075*o*pc)) != 0):
                        print("P-Min Twin-Primes:",(n/(n/(round(n*r2)-round(0.04474*o*pc)))),"Actual Number Of Twin-Primes:",z2,"P-Max Twin-Primes:",(n/(n/(round(n*r2)-round(0.00122*o*pc)))))
                        if((n/(n/(round(n*r2)-round(0.04474*o*pc))))>z2):
                            print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")            
            if(round(n/n*r3 != 0)):
                if((round(n*r3)-round(0.004771*o*pc)) != 0):
                    if(n/(round(n*r3)-round(0.004771*o*pc)) != 0):
                        print("P-Min Trip-Primes:",(n/(n/(round(n*r3)-round(0.004771*o*pc)))),"Actual Number Of Trip-Primes:",z3,"P-Max Trip-Primes:",(n/(n/(round(n*r3)-round(-0.0017*o*pc)))))
                        if((n/(n/(round(n*r3)-round(0.004771*o*pc))))>z3):
                            print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    p=p+o
    o=2