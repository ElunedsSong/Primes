import math


def is_prime(n):
    """
    Checks if a number is prime.

    Args:
      n: The number to check.

    Returns:
      True if n is prime, False otherwise.
    """
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print("I think 11 is prime?", is_prime(71-60))


def find_primes_between(start, end):
    """
    Finds all prime numbers between two numbers (inclusive).

    Args:
      start: The starting number.
      end: The ending number.

    Returns:
      A list of prime numbers between start and end.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def test_hypothesis(hcn1, hcn2):
    """
    Tests the hypothesis: 
      1. Find all prime numbers between two consecutive highly composite numbers.
      2. Subtract the sum of these primes from the larger HCN.
      3. Check if the result is prime.

    Args:
      hcn1: The first highly composite number.
      hcn2: The second highly composite number.

    Returns:
      True if the result is prime, False otherwise.
    """
    primes_between = find_primes_between(hcn1, hcn2)
    a = len(primes_between)
    q = 0
    while (q < a-1):
        if (is_prime(primes_between[q]-hcn1) == False):
            print(primes_between[q], primes_between[q]-hcn1)
            return False
        if (is_prime(primes_between[q]-hcn1) == True):
            q = q+1
    return True


# Example usage:
highly_composite_numbers = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840,
                            1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160]

for i in range(len(highly_composite_numbers) - 1):
    hcn1 = highly_composite_numbers[i]
    hcn2 = highly_composite_numbers[i + 1]
    if test_hypothesis(hcn1, hcn2):
        print(f"For HCN1={hcn1} and HCN2={hcn2}, the result is prime.")
    else:
        print(f"For HCN1={hcn1} and HCN2={hcn2}, the result is not prime.")
