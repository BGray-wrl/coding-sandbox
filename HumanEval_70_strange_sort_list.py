
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return []

    sorted_list = sorted(lst)
    result = []
    left = 0
    right = len(sorted_list) - 1
    is_min_turn = True

    while left <= right:
        if is_min_turn:
            result.append(sorted_list[left])
            left += 1
        else:
            result.append(sorted_list[right])
            right -= 1
        is_min_turn = not is_min_turn
    return result
