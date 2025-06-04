def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        # For n-digit numbers:
        # Count of numbers starting with 1: 1 * 10^(n-1)
        # Count of numbers ending with 1: 9 * 10^(n-2) (first digit can be 1-9, last digit is 1)
        # Count of numbers starting AND ending with 1: 1 * 10^(n-2) (first digit is 1, last digit is 1)

        # Using the principle of inclusion-exclusion:
        # Total = (Numbers starting with 1) + (Numbers ending with 1) - (Numbers starting AND ending with 1)
        # Total = 10**(n-1) + (9 * 10**(n-2)) - 10**(n-2)
        # Total = 10 * 10**(n-2) + 9 * 10**(n-2) - 1 * 10**(n-2)
        # Total = (10 + 9 - 1) * 10**(n-2)
        # Total = 18 * 10**(n-2)
        return 18 * (10**(n-2))