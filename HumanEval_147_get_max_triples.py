def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k,
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation:
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    count_mod_0 = 0
    count_mod_1 = 0

    # Analyze a[i] = i * i - i + 1 modulo 3
    # If i % 3 == 0: a[i] % 3 = (0*0 - 0 + 1) % 3 = 1
    # If i % 3 == 1: a[i] % 3 = (1*1 - 1 + 1) % 3 = 1
    # If i % 3 == 2: a[i] % 3 = (2*2 - 2 + 1) % 3 = (4 - 2 + 1) % 3 = 0

    for i in range(1, n + 1):
        if i % 3 == 2:
            count_mod_0 += 1
        else: # i % 3 == 0 or i % 3 == 1
            count_mod_1 += 1

    # Helper function to calculate combinations C(n, k)
    def combinations(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        if k > n // 2:
            k = n - k

        res = 1
        for i in range(k):
            res = res * (n - i) // (i + 1)
        return res

    # A sum (a[i] + a[j] + a[k]) is a multiple of 3 if:
    # 1. All three elements a[i], a[j], a[k] are 0 (mod 3)
    # 2. All three elements a[i], a[j], a[k] are 1 (mod 3)
    # (Other combinations like 0+0+1, 0+1+1, etc. will not result in 0 mod 3)

    result = combinations(count_mod_0, 3) + combinations(count_mod_1, 3)
    return result