def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    float_val = float(value)

    # If the number is already an integer, return it directly
    if float_val == int(float_val):
        return int(float_val)

    # Determine the floor and ceiling integers based on the sign of float_val
    if float_val >= 0:
        floor_val = int(float_val)
        ceil_val = floor_val + 1
    else:  # float_val < 0
        ceil_val = int(float_val)
        floor_val = ceil_val - 1

    # Calculate the absolute differences to the floor and ceiling integers
    diff_floor = abs(float_val - floor_val)
    diff_ceil = abs(float_val - ceil_val)

    # Compare differences and return the closest integer
    if diff_floor < diff_ceil:
        return floor_val
    elif diff_ceil < diff_floor:
        return ceil_val
    else:  # Equidistant, round away from zero
        if float_val > 0:
            return ceil_val
        else:  # float_val < 0
            return floor_val