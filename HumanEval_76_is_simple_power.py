def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Handle specific cases for n
    if n == 1:
        return x == 1
    
    # If n is 0, x must be 0 (for positive integer exponent) or 1 (for 0 exponent, 0**0 = 1)
    # The problem implies non-negative integer exponents.
    if n == 0:
        return x == 0 or x == 1
    
    # At this point, n is guaranteed to be a positive integer >= 2 based on problem context
    # (negative n is not implied by examples, and adds complexity for signed x).
    
    # If x is 0 and n is not 0, n**int cannot be 0.
    if x == 0:
        return False
        
    # If x is 1, any non-zero n raised to the power of 0 is 1.
    if x == 1:
        return True
    
    # Now, x is guaranteed to be >= 2 and n is guaranteed to be >= 2.
    # We check if x can be repeatedly divided by n until it reaches 1.
    temp_x = x
    while temp_x % n == 0:
        temp_x //= n
    
    # If, after all possible divisions, temp_x is 1, then x was a simple power of n.
    return temp_x == 1