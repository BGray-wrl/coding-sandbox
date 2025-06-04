def pluck(arr):
    smallest_even = float('inf')
    smallest_even_index = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0:  # Check if the number is even
            if arr[i] < smallest_even:
                smallest_even = arr[i]
                smallest_even_index = i

    if smallest_even_index == -1:  # No even numbers found
        return []
    else:
        return [smallest_even, smallest_even_index]