import sympy

x = 4
z = 100000
ratio = 1

total = 0

numofloops = 0


def twin_primes_to_x(n):
    p = 5
    totalp = 0
    temptotal = 1
    ratio = 1
    while (p < n):
        ratio = ratio*((p-2)/p)
        o = 2
        totalp = totalp+1
        if (sympy.isprime(p+o == True)):
            temptotal = temptotal+1
        while (sympy.isprime(p+o) != True):
            o = o+2

        p = p+o

    return totalp


while (x < z):
    ratio = ratio * ((x-2)/x)
    x = x+4


def primes_to_x(n):
    p = 5
    totalp = 1
    while (p < n):
        o = 2
        totalp = totalp+1
        if (sympy.isprime(p+o == True)):
            temptotal = temptotal+1
        while (sympy.isprime(p+o) != True):
            o = o+2

        p = p+o

    return totalp


n = primes_to_x(z)

print('For:', x, 'x*ratio=', (x-n)*ratio)
