from collections import Counter
import math


def primes_up_to(limit):
    """Generates a list of prime numbers up to a given limit."""
    if limit < 2:
        return []
    primes = [2]
    for num in range(3, limit + 1, 2):  # Check only odd numbers
        is_prime = True
        for p in primes:
            if p * p > num:  # Optimization: only check up to sqrt(num)
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def prime_factors(x):
    factors = []
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors.append(d)
            x //= d
        d += 1
    if x > 1:
        factors.append(x)
    return factors


def prime_facto(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n):
    if n < 1:
        return False
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_unique_prime_factors(n, primes):
    """Counts the number of unique prime factors and returns the smallest."""
    factors = []
    for p in primes:
        if n % p == 0:
            factors.append(p)
    factors = sorted(list(set(factors)))
    if factors:
        smallest_factor = factors[0]
    else:
        smallest_factor = float('inf')  # Handle cases with no prime factors
    # Return the smallest factor, the count, and the factors
    return smallest_factor, len(factors), factors


def generate_products(primes, x):
    final_list = []

    if not primes or primes[0] >= x:
        return []

    first_prime = primes[0]
    must_include = [first_prime]
    min_other_prime = first_prime
    if x > 150 and len(primes) >= 2 and first_prime * primes[1] < x:
        second_prime = primes[1]
        must_include.append(second_prime)
        min_other_prime = second_prime

    def generate_multiples(current_multiple, remaining_primes):
        if current_multiple >= x:
            return
        if current_multiple not in final_list:
            final_list.append(current_multiple)

        for i in range(len(remaining_primes)):
            p = remaining_primes[i]
            new_multiple = current_multiple
            while new_multiple * p < x:
                new_multiple *= p
                if new_multiple not in final_list:
                    generate_multiples(new_multiple, remaining_primes[i+1:])

    initial_multiple = 1
    for p in must_include:
        initial_multiple *= p

    if initial_multiple < x:
        final_list.append(initial_multiple)  # Add the initial multiple here!
        generate_multiples(initial_multiple, [
                           p for p in primes if p >= min_other_prime and p not in must_include])

    final_list.sort(key=lambda n: len(set(prime_facto(n, primes))))
    return final_list


# ... (main function and example usage remain the same)


def main(x, r):
    checker = 0
    all_factors = prime_factors(x)
    sqrt_limit = int(math.sqrt(x))
    sqrt_primes = primes_up_to(sqrt_limit)

    unique_primes = []
    for factor in sqrt_primes:  # Iterate through sqrt_primes
        if factor not in all_factors:
            unique_primes.append(factor)
    if (checker == 0):
        print(unique_primes)

    final_list = generate_products(unique_primes, x)
    final_list = list(set(final_list))  # Remove duplicates before sorting)
    if (checker == 0):
        print(final_list)
    if (len(final_list) == 0):
        final_list.append(1)
    qr = 0
    total = 0
    prime_count = 0
    if final_list:
        for num in final_list:
            if (qr < r):
                if is_prime(x - num):
                    prime_count += 1
                if is_prime(x + num):
                    prime_count += 1
            qr = qr+1
            total = total+2
            if (qr+1 == r):
                break

        percentage = (prime_count / (total))*100
    else:
        percentage = 0
    return percentage


x = 10
zn = 300
r = 1
totalwin = 0
totaltotal = 0

while (x < zn):
    if (is_prime(x) == False):
        totaltotal = totaltotal+1
        percentage = 0
        while (percentage < 50.0001):
            percentage = main(x, r)
            r = r+1
            if (r > 25):
                print("Bad!!!!!!!!!!!!!!")
                percentage = 52
                totalwin = totalwin+1

        print(f"For x = {x}, the prime percentage is: {percentage:.2f}%")
    x = x+1
    r = 1


print('Total Success rate:', 1-totalwin/totaltotal)
