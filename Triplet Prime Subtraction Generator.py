import math

import sympy

o=2
p=5
pc=2
r=1/6
i=5
lp=0
average= 0
averaget=0
minimumaverage=1
maximumaverage=-500000000000


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


            PrimeCount=0
            z=0
            k=-10
            u=0


            while (i<a+1):
                if (sympy.isprime(i) == True):
                    r=r*((i-3)/i)
                    PrimeCount=PrimeCount+1
                i=i+1
  
            u=n/(round(n*r))


            while (q<(y-1)):
                if (sympy.isprime(q)==True):
                    q=q+2
                    if(sympy.isprime(q)==True):
                        q=q+4
                        if(sympy.isprime(q)==True):
                            z=z+1
                        q=q-4
                    q=q-2    
                q=q+1

            if (z!=0):
                if (u==n/z):
                    k=0
                    
                while(u!=n/z):
                    k=k+1
                    u=n/(round(n*r-k))
                
                print("Between:",p,"and:",p+o,"subtraction value:",(k/o/pc))
                averaget=averaget+1
                average = average + (k/o/pc)
                
                if(a>18000):
                    if ((k/o/pc)<minimumaverage):
                        minimumaverage=k/o/pc
                    if ((k/o/pc)>maximumaverage):
                        maximumaverage=k/o/pc
                print("Average Subtraction Value: ", average/ averaget, "Minimum Subtraction Value: ", minimumaverage,"Maxmium Subtraction Value: ", maximumaverage)
        p=p+o
    o=2