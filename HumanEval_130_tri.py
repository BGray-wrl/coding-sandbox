def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n < 0:
        return []

    trib = [0] * (n + 1)

    if n >= 0:
        trib[0] = 1
    if n >= 1:
        trib[1] = 3

    # Populate even numbers first
    for i in range(2, n + 1):
        if i % 2 == 0:  # i is even
            trib[i] = 1 + i // 2

    # Populate odd numbers using the already calculated values
    for i in range(2, n + 1):
        if i % 2 == 1:  # i is odd
            tri_next_val = 0
            if i + 1 <= n:
                tri_next_val = trib[i+1]
            else:
                # If i+1 is outside the requested range (i.e., i == n),
                # but needed for the calculation of tri(n), calculate it on the fly.
                # Since i is odd, i+1 is even, so use the even rule.
                tri_next_val = 1 + (i + 1) // 2

            trib[i] = trib[i-1] + trib[i-2] + tri_next_val

    return trib