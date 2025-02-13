import math
import sympy


def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(x):
    """Returns a list of prime factors of x."""
    factors = []
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors.append(d)
            x //= d
        d += 1
    if x > 1:
        factors.append(x)
    return list(set(factors))  # Remove duplicates


def primes_up_to_sqrt(x):
    """Returns a list of primes up to the square root of x."""
    limit = int(math.sqrt(x)) + 1
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes


def other_primes(x):
    """Returns primes up to sqrt(x) that are NOT factors of x."""
    factors = prime_factors(x)
    primes = primes_up_to_sqrt(x)
    return [p for p in primes if p not in factors]


r = 10
fn = 500
list_of_lists = other_primes(r)
qn = len(list_of_lists)
x = 0
uz = 0
plusminus = 1
totalacc = 0
total = 0

checker_list = []
checkervar = 1
if (checkervar == 0):
    print(list_of_lists)
while (r < fn):
    while (x < qn+1):
        if (uz < x):
            plusminus = plusminus*list_of_lists[x-1]
        if (sympy.isprime(r-plusminus) == True):
            totalacc = totalacc+1
        if (sympy.isprime(r+plusminus) == True):
            totalacc = totalacc+1
        if (checkervar == 0):
            checker_list.append(r-plusminus)
            checker_list.append(r+plusminus)
        if (x == 0):
            if (r % 2 == 1):
                total = total-2
        total = total+2
        x = x+1
        if (x > 0):
            if x < qn+1:
                if (plusminus*list_of_lists[x-1]+1 > r):
                    x = x+qn+1
    if (totalacc/total < .501):
        print('For', r, 'percent prime is: ', totalacc/total)
    x = 0
    uz = 0
    plusminus = 1
    totalacc = 0
    total = 0
    r = r+1
    if (sympy.isprime(r) == True):
        r = r+1
    list_of_lists = other_primes(r)
    qn = len(list_of_lists)

print(checker_list)
