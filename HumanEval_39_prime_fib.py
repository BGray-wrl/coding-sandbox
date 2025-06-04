def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_fib_numbers():
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b

    count = 0
    fib_gen = generate_fib_numbers()
    
    # Skip the first two Fibonacci numbers (0 and 1) if they are not considered prime
    # The examples start with 2, which is the 3rd fibonacci number (0, 1, 1, 2)
    # The fib_gen yields b, so it will yield 1, 1, 2, 3, 5, ...
    # We want the first prime fibonacci number to be 2, so we need to handle this.
    # The sequence of fibonacci numbers that are prime: 2, 3, 5, 13, 89
    
    # Consume initial 1s (from 0, 1, 1, 2, ...) if n > 0 and 1 is not prime.
    # The function starts with b=1.
    # The first number yielded is 1. If n=1, we don't want 1.
    # The examples show that for n=1, the result is 2.
    
    # Adjusting the fibonacci generator to start from 2 effectively
    # Or, check the numbers after 1 (which is not prime).
    
    while True:
        fib_num = next(fib_gen)
        # Skip 1 as it's not prime and the sequence starts from 2 in examples
        if fib_num == 1:
            continue
        
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num