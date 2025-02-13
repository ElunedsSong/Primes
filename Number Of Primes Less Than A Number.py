import sympy

ratio = 1/2


n = 10000

p = 11
total = 1


def totalizer(p):

    newp = p*p
    total = 1
    p = 3
    while (p < newp+1):
        o = 2
        while (sympy.isprime(p+o) != True):
            o = o+2
        total = total+1

        p = p+o
    return (total)


def get_ratio_and_compare_to_observed_primes(p):
    o = 2
    originalp = p
    p = 3
    ratio = 1/2
    while (p < originalp+1):
        o = 2
        while (sympy.isprime(p+o) != True):
            o = o+2
        ratio = ratio * ((p-2)/p)

        p = p+o
    newtotal = totalizer(originalp)

    print("For: ", originalp, "ratio is:", ratio,
          'and the total for', originalp*originalp, 'is: ', newtotal, "making the implied ratio:", originalp*originalp*ratio)


while (p < n):
    o = 2
    if (p == 2):
        o = 0
        p = 3
    while (sympy.isprime(p+o) != True):
        o = o+2
    get_ratio_and_compare_to_observed_primes(p)
    if (p == 3):
        o = 2

    p = p+o
