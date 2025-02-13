import math
from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return list(set(factors))


def primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def largest_combinations(non_shared_primes, x, zn):
    if not non_shared_primes:
        return []

    first_prime = non_shared_primes[0]
    n = len(non_shared_primes)
    all_combinations = []

    for r in range(1, n + 1):
        for indices in combinations(range(1, n), r - 1):
            comb = [first_prime] + [non_shared_primes[i] for i in indices]
            if math.prod(comb) < x:
                all_combinations.append(comb)

    # Sort by length (largest combinations first)
    all_combinations.sort(key=len, reverse=True)

    final_result = []
    if all_combinations:
        max_len = len(all_combinations[0])
        qz = 0
        for comb in all_combinations:
            if len(comb) > max_len-2:
                qz = qz+1
                if (qz < zn):
                    final_result.append(comb)
            else:
                break  # Stop checking once we hit a shorter length

    return final_result


def check_primality(x, combinations):
    successes = 0
    total = 0
    for comb in combinations:
        product = 1
        for num in comb:
            product *= num
        if is_prime(x + product):
            successes += 1
        if is_prime(x - product):
            successes += 1
        total += 2
    if total == 0:
        return 0
    return (successes / total) * 100


def main_function(x, qr):
    x = int(x)
    prime_factors_of_x = prime_factors(x)
    primes_to_sqrt_x = primes_up_to(int(x))
    non_shared_primes = [
        p for p in primes_to_sqrt_x if p not in prime_factors_of_x]
    if not non_shared_primes:
        return 0
    combinations = largest_combinations(non_shared_primes, x, qr)
    print(combinations)
    primality_percentage = check_primality(x, combinations)
    return primality_percentage


# Example usage:
x = 10
zn = 100
r = 2
totalwin = 0
totaltotal = 0

while (x < zn):
    if (is_prime(x) == False):
        totaltotal = totaltotal+1
        percentage = 0
        while (percentage < 50.0001):
            percentage = main_function(x, r)
            r = r+1
            if (r > 20):
                print("Bad!!!!!!!!!!!!!!")
                percentage = 52
                totalwin = totalwin+1

        print(f"For x = {x}, the prime percentage is: {percentage:.2f}%")
    x = x+1
    r = 2


print('Total Success rate:', 1-totalwin/totaltotal)
