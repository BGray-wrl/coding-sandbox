def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = -1

    for num in lst:
        if is_prime(num):
            if num > largest_prime:
                largest_prime = num

    sum_digits = 0
    if largest_prime != -1:
        for digit in str(largest_prime):
            sum_digits += int(digit)
    return sum_digits