import math

import sympy

w = 0
o = 2
p = 7
z = 1
list_of_lists = []
primemod = 11
q = 97
i = 0
new_list = []

while (w == 0):
    while (q < 100000000):
        if (sympy.isprime(q) == True):
            q = q+4
            if (sympy.isprime(q) == True):
                q = q+2
                if (sympy.isprime(q) == True):
                    q = q+4
                    if (sympy.isprime(q) == True):
                        q = q+2
                        if (sympy.isprime(q) == True):
                            q = q+4
                            if (sympy.isprime(q) == True):
                                list_of_lists.append(q-16)
                            q = q-4
                        q = q-2
                    q = q-4
                q = q-2
            q = q-4
        q = q+2
    while (primemod < 1000):
        print("modular options for", primemod)
        new_list.extend(list_of_lists)
        while i < len(new_list):
            new_list[i] = (((new_list[i]-97)//210) % primemod)
            i = i+1
        new_new_list = list(set(new_list))
        new_new_list.sort()
        print(new_new_list)
        new_list.clear()
        new_new_list.clear()
        primemod = primemod+2
        while (sympy.isprime(primemod) != True):
            primemod = primemod+2
        i = 0
        w = 1
    p = p+o
    o = 2
