def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    found_odd_digit = False
    for digit_char in str(n):
        digit = int(digit_char)
        if digit % 2 != 0:
            product *= digit
            found_odd_digit = True
    
    if found_odd_digit:
        return product
    else:
        return 0