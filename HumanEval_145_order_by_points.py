def order_by_points(nums):
    def get_sum_of_digits(n):
        s = 0
        # Convert to string and take absolute value to handle negative numbers
        # and sum the digits.
        for digit_char in str(abs(n)):
            s += int(digit_char)
        return s

    # Create a list of tuples: (sum_of_digits, original_index, number)
    # This allows sorting by sum of digits first, then by original index for tie-breaking.
    indexed_nums = []
    for i, num in enumerate(nums):
        sum_digits = get_sum_of_digits(num)
        indexed_nums.append((sum_digits, i, num))

    # Sort the list of tuples. Python's default tuple comparison sorts
    # by the first element, then the second, and so on.
    sorted_indexed_nums = sorted(indexed_nums)

    # Extract the original numbers from the sorted list
    result = [item[2] for item in sorted_indexed_nums]

    return result