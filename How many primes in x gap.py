import sympy
import math


y = 6

z = 1000000000000
n = 2
u = 10000
p = 2
total = 0
prevtotal = -1
while (u < z):
    while (p < n):
        o = 2
        if (p == 2):
            o = 0
            p = 3
        while (sympy.isprime(p+o) != True):
            o = o+2
        total = total+1
        p = p+o
    p = 2
    u = n
    if (prevtotal < total):
        if (prevtotal * math.sqrt(2) < total):
            if (prevtotal != 0):
                print("Number of Primes less than ", n,
                      "Matches expectation", total, "Compared to Previous Total", total/(prevtotal*math.sqrt(2)))
        else:
            print("Failure!!!!")
    else:
        print("Number of primes less than ", n,
              prevtotal, total, "Failure!!!!!")
    prevtotal = total
    total = 0
    n = n*2
