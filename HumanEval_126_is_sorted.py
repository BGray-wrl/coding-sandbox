def is_sorted(lst):
    counts = {}
    for i in range(len(lst)):
        num = lst[i]
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] > 2:
            return False

        if i > 0 and lst[i] < lst[i-1]:
            return False
    return True