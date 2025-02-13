import math

import sympy


i=2
u=3
o=2
a=1
z=2
k=0
v=3

factorizedsum =1
number=3
while(number<100000000000000000000):
    o=2
    while(sympy.isprime(v+o) != True):
                o=o+2
    v=v+o        
    number=number*(v)
    while(i<=number+1):
        k=0
        if(i<=number+1):
            if(number%i==0):
                factorizedsum= factorizedsum + number/i
                factorizedsum= factorizedsum + i
                print(i)
        if (number%i!=0):
            i=round(i**(1/a))
            o=2
            if (i==2):
                z=z+1
                i=i+1
                o=0
            while(sympy.isprime(i+o) != True):
                o=o+2
            i=i+o
            z=i+o
            a=1
            k=1
        if (k==0):    
            if ((number/i)%i==0):
                if((z**(a+1))>(number)+1):
                    i=round(i**(1/a))
                    o=2
                    if (i==2):
                        z=z+1
                        i=i+1
                        o=0
                    while(sympy.isprime(i+o) != True):
                        o=o+2
                    i=i+o
                    z=i+o
                    a=1
                    k=1
                if((z**(a+1))<=(number)+1):
                    i=z**(a+1)
                    a=a+1
            if ((number/i)%i!=0):
                i=round(i**(1/a))
                o=2
                if (i==2):
                    z=z+1
                    i=i+1
                    o=0
                while(sympy.isprime(i+o) != True):
                    o=o+2
                i=i+o
                z=i+o
                a=1
                k=1

    if(factorizedsum>number*95/100):
        if(factorizedsum<number*105/100):
            print("Perfect-ish odd number !!!!!!!!!!!!!!!!!")
    print("Sum of Factors of",number, "is",factorizedsum, "F-%:",factorizedsum/number)

    factorizedsum=1
    a=1
    i=2
    z=2
    o=2
    
print("Done")