

import sympy


qi = 1
qz = 0

while (qi < 100000):
    if (sympy.isprime((qi)) == True):
        if (sympy.isprime(2**(qi)-1) != True):
            print(qi, qz)
            qz = qz+1
    if (sympy.isprime(2**(qi)-1) == True):
        qz = qz+1
    qi = qi+1
