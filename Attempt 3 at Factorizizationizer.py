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
p=2

divisors_list = [1]
partialmulti_list = [1]


factorizedsum =1
number=3
while(number<100000000000000):
    o=2
    while(sympy.isprime(v+o) != True):
                o=o+2
    v=v+o        
    number=number*(v)
    if(sympy.isprime(number) == True):
        g=1
    if(g==0):
        while(p<=math.sqrt(number)):
            z=p
            while(number%p==0):
                if(number!=p):
                    divisors_list.append(number/p)
                    divisors_list.append(p)
                p=p**(a+1)
                a=a+1
            p=z
            a=1
            o=2
            if (p==2):
                p=p+1
                o=0
            while(sympy.isprime(p+o) != True):
                o=o+2
            p=p+o   
    divisors_list = list(set(divisors_list))
    factorizedsum = sum(divisors_list)     
    print("Sum of Factors of",number, "is",factorizedsum, "F-%:",factorizedsum/number)
    g=0
    p=2
    divisors_list.clear()
    divisors_list = [1]
    
print("Done")