import math

import sympy

o=2
p=5
pc=2
r=1
i=2
average= 0
averaget=0
minimumaverage=1
maximumaverage=-500000000


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


            
            averaget=averaget+1
            print("Between:",p,"and:",p+o,"subtraction value:",(k/(o)/pc))
            average = average + (k/o/pc)
            if(a>100):
                if ((k/o/pc)<minimumaverage):
                    minimumaverage=k/o/pc
                if ((k/o/pc)>maximumaverage):
                    maximumaverage=k/o/pc
            print("Average Subtraction Value: ", average/ averaget, "Minimum Subtraction Value: ", minimumaverage,"Maxmium Subtraction Value: ", maximumaverage)
            
    p=p+o
    o=2