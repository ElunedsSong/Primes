from collections import Counter
from itertools import product


def prime_factors(n):
    factors = []
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd at this point, check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors


def generate_factors(prime_factors):
    factor_count = Counter(prime_factors)
    unique_primes = list(factor_count.keys())
    prime_exponents = [range(count + 1) for count in factor_count.values()]

    factors = set()

    # Generate all combinations of prime factors with their exponents
    for exponents in product(*prime_exponents):
        product_factor = 1
        for prime, exponent in zip(unique_primes, exponents):
            product_factor *= prime ** exponent
        factors.add(product_factor)

    return sorted(factors)


# Example usage
number = int(input("Enter a number: "))
pfactors = prime_factors(number)
z = sum(generate_factors(pfactors))
q = z-number

print(z)
print(q)
print(q/number)

print("Prime factors of", number, ":", pfactors)
print("Factors of", number, ":", generate_factors(pfactors))
