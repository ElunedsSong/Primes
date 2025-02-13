import math

import sympy


i=2
u=3
o=2
a=1
z=2
k=0
v=3
p=1
g=0

divisors_list = [1]


factorizedsum =1
number=3
while(number<106):
    o=2
    while(sympy.isprime(v+o) != True):
                o=o+2
    v=v+o        
    number=number*(v)
    p=round(math.sqrt(number))+2
    if (p%2==0):
        p=p-1
    while(p>0):
        o=2
        if (p==2):
            p=-1
            o=2
        if (p==3):
            o=0
            p=2
        if(p>4):
            while(sympy.isprime(p-o) != True):
                o=o+2
        p=p-o
        g=p
        while(p>0):
            if(number%p==0):
                divisors_list.append(number/p)
                divisors_list.append(p)
            o=2
            if (p==2):
                p=-1
                o=2
            if (p==3):
                o=0
                p=2
            if(p>4):
                while(sympy.isprime(p-o) != True):
                    o=o+2
            p=p-o
        p=g
    divisors_list = list(set(divisors_list))
    factorizedsum = sum(divisors_list)
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