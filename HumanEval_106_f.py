def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            fact = 1
            for k in range(1, i + 1):
                fact *= k
            result.append(fact)
        else:
            s = i * (i + 1) // 2
            result.append(s)
    return result