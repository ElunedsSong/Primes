import math

import sympy

o=2
p=5

PrimeCount=2

while(p<7000):
    if (sympy.isprime(p) == True):
        while(sympy.isprime(p+o) != True):
            o=o+2
        if (sympy.isprime(p+o) == True):
            PrimeCount=PrimeCount+1
            a=p
            t=o
            b=a+t
            q=a*a
            y=b*b
            n=y-q

            print("For ",a,"To ",b, "Which is a^2 ",q,"to b^2",y)

            i=2
            r=1
            z=0
            k=0


            while (q<(y-1)):
                if (sympy.isprime(q)==True):
                    q=q+2
                    if (sympy.isprime(q)==True):
                        z=z+1
                    q=q-2
                q=q+1

            if (round((n/((PrimeCount)*12))-1)>0):
                print("Predicted Ratio of T-Primes:",(n/(round(n/((PrimeCount-1)*12))-1)),"Predicted Number Of T-Primes:",(n/(n/(round(n/((PrimeCount-1)*12))-1))))
                print("PrimeCount: ",PrimeCount,"Actual Ratio of Primes", n/z,"Actual Number Of Primes:",z)
                print("     ") 
            if (round((n/((PrimeCount)*12))-1)<=0):
                print("Predicted Ratio of T-Primes:","0","Predicted Number Of T-Primes:","0")
                print("PrimeCount: ",PrimeCount,"Actual Ratio of Primes", n/z,"Actual Number Of Primes:",z)
                print("     ") 
                

    p=p+o
    o=2