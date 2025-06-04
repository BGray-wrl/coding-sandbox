def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1

    # Divide by 2 until n is odd
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Iterate for odd factors from 3 up to sqrt(n)
    # We only need to check up to the square root of n
    # because if n has a prime factor larger than sqrt(n),
    # it must also have a prime factor smaller than sqrt(n).
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_factor = i
            n //= i
        i += 2  # Check next odd number

    # If n is still greater than 1 after the loop,
    # it means the remaining n is a prime number itself,
    # and it must be the largest prime factor.
    if n > 1:
        largest_factor = n

    return largest_factor