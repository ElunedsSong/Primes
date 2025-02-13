import sympy


def twin_primes_to_xr(n):
    p = 5
    total = 0

    while (p < n):
        o = 2
        if (sympy.isprime(p+o) == True):
            total = total+1
        while (sympy.isprime(p+o) != True):
            o = o+2

        p = p+o

    return total


print(twin_primes_to_xr(524119*6))


def twin_primes_to_x(n):
    p = 5
    ratio = 1

    while (p < n):
        o = 2
        ratio = ratio*(p-2)/p

        x = twin_primes_to_xr(p*6)

        print(p, ratio, 6*x)

        while (sympy.isprime(p+o) != True):
            o = o+2

        p = p+o

    return
