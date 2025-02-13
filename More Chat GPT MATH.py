import math


def is_prime(n):
    """Efficiently checks if a number is prime."""
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


def prime_generator(limit):
    """Generates prime numbers up to a limit using Sieve of Eratosthenes."""
    primes = []
    is_prime_list = [True] * (limit + 1)
    is_prime_list[0] = is_prime_list[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_list[i]:
            for multiple in range(i*i, limit + 1, i):
                is_prime_list[multiple] = False

    for i in range(2, limit+1):
        if is_prime_list[i]:
            primes.append(i)
    return primes


def prime_ratio_product_optimized(limit):
    """Calculates the product of p/(p-2) for primes up to a limit and counts twin primes."""
    if limit < 3:
        return 1, 0  # No primes suitable for the ratio below 3, no twin primes

    primes = prime_generator(limit)
    product = 1.0
    twin_prime_count = 0

    for i in range(len(primes)):
        p = primes[i]
        if p >= 3:
            product *= (p / (p - 2))

        if i > 0 and primes[i] - primes[i-1] == 2:  # check for twin primes
            twin_prime_count += 1

    return product, twin_prime_count


# Example usage:
limit = 100000000  # Example limit
result, twin_count = prime_ratio_product_optimized(limit)
print(
    f"The product of p/(p-2) for primes up to {limit} is approximately: {result}")
print(f"Number of twin primes found up to {limit}: {twin_count}")

print(limit/result)
