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


j=(math.log(a*a,12))-1



while (i<math.sqrt(((q)))):
    if (sympy.isprime(i) == True):
        r=r*((i-2)/i)
        PrimeCount=PrimeCount+1
    i=i+1

r=r/6



ln=math.log(a*a)
ln2=ln*ln
print (ln2)

ln3= (ln2+1/r)/2

while (a<b):
    if (sympy.isprime(a)==True):
        lm=lm+1
    a=a+1


while (q<(y-1)):
    if (sympy.isprime(q)==True):
        z=z+1
    q=q+1
print("Prime Count:",PrimeCount)
print("r value:",r)
print ("Predicted Count:",r*n)
print (n)
print("Actual Number of Primes: ",z)
print ("Twin Prime Count:",z)
print ("Actual Ratio:",n/z)
print("Predicted r ratio:", 1/r)
print ("Averaged log ratio:",ln3)

print("Primes between: ",a,"and: ",b,lm)
