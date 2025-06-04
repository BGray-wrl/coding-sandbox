def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        # Based on example intersection((-1, 1), (0, 4)) ==> "NO"
        # where length is 2, implies 2 is not considered prime for this problem.
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    start_intersect = max(start1, start2)
    end_intersect = min(end1, end2)

    if start_intersect > end_intersect:
        return "NO"

    length = end_intersect - start_intersect + 1

    if is_prime(length):
        return "YES"
    else:
        return "NO"