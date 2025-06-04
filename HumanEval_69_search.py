def search(lst):
    freq_map = {}
    for num in lst:
        freq_map[num] = freq_map.get(num, 0) + 1

    result = -1
    for num, count in freq_map.items():
        if num > 0 and count >= num:
            result = max(result, num)
    return result