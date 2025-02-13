import sympy


n = 1000


def ratio_between_prime_square_gap(n, r):
    total = 0
    f = r*r
    p = n*n
    actualtotal = f-p-1

    while (p < f):
        o = 2
        while (sympy.isprime(p+o) != True):
            o = o+2
        p = p+o
        if (p < f):
            total = total+1

    return (total/actualtotal)


ratio = 1/2
p = 3
while (p < n):
    o = 2
    ratio = ratio*(p-1)/p
    oldp = p
    while (sympy.isprime(p+o) != True):
        o = o+2
    p = p+o

    newratio = ratio_between_prime_square_gap(oldp, p)

    print("Ratio for", oldp, "to", p, ratio, "and", newratio)
