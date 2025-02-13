
import sympy

list_of_fake_primes = []

list_of_times_two_but_real = []


qi = 5

while (qi < 25000):
    qi = qi*2 + 1

    if (sympy.isprime(qi) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, "is a false prime")
        else:
            print(qi, "is not a false prime")

qi = 14

while (qi < 25000):
    qi = qi*2 + 1

    if (sympy.isprime(qi) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, "is a false prime")
        else:
            print(qi, "is not a false prime")


qi = 18

while (qi < 25000):
    qi = qi*2 + 1

    if (sympy.isprime(qi) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, "is a false prime")
        else:
            print(qi, "is not a false prime")

qi = 20

while (qi < 25000):
    qi = qi*2 + 1

    if (sympy.isprime(qi) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, "is a false prime")
        else:
            print(qi, "is not a false prime")

qi = 21

while (qi < 25000):
    qi = qi*2 + 1

    if (sympy.isprime(qi) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, "is a false prime")
        else:
            print(qi, "is not a false prime")


qi = 26

while (qi < 25000):
    qi = qi*2 + 1

    if (sympy.isprime(qi) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, "is a false prime")
        else:
            print(qi, "is not a false prime")
