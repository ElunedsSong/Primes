import math

import sympy



a= 5000
t=5000
b=a+t
q=a*a
y=b*b
n=y-q


PrimeCount=0
i= 5
r=1
u=2
z=0
k=0
l=1
x=1
ln=0
ln=2
lm=0
lo=0



while (a<b):
    if (sympy.isprime(a)==True):
        lm=lm+1
    a=a+1

print("Primes between: ",a,"and: ",b,lm)
