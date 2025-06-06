def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    else:
        actual_shift = shift % n  # Handle cases where shift is a multiple of n
        return s[n - actual_shift:] + s[:n - actual_shift]