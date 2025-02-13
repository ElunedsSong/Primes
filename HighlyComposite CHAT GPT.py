from math import sqrt


def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def num_divisors(n):
    """Calculates the number of divisors of a number."""
    count = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            count += 2  # Count i and n/i
    if int(sqrt(n)) * int(sqrt(n)) == n:
        count -= 1  # Avoid double-counting the square root
    return count


def generate_hcn(limit):
    """Generates a list of highly composite numbers up to a given limit."""
    hcn_list = [1]  # 1 is not a prime, but it's a starting point
    for n in range(2, limit + 1):
        if all(num_divisors(n) > num_divisors(i) for i in range(1, n)):
            hcn_list.append(n)
    return hcn_list


# Generate a list of highly composite numbers up to 1000
hcn_list = generate_hcn(100000)
print(hcn_list)
