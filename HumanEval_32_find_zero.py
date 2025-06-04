import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    f = lambda x_val: poly(xs, x_val)

    # Find an initial interval [low, high] where f(low) and f(high) have opposite signs.
    # We will expand the interval starting from a small range.
    low = -1.0
    high = 1.0

    # Expand the interval until a sign change is found or a boundary is a root.
    max_interval_search_steps = 100
    for _ in range(max_interval_search_steps):
        # Using a small tolerance for float comparison to check for exact roots at boundaries
        if abs(f(low)) < 1e-9:
            return low
        if abs(f(high)) < 1e-9:
            return high

        if f(low) * f(high) < 0:
            break

        low *= 2
        high *= 2
        if abs(low) > 1e18 or abs(high) > 1e18:
            raise ValueError("Interval search diverged, unable to find a root within practical limits.")

    # Bisection method to find the root within the found interval
    tolerance = 1e-7
    max_bisection_iterations = 500

    for _ in range(max_bisection_iterations):
        mid = (low + high) / 2
        f_mid = f(mid)

        if abs(f_mid) < tolerance:
            return mid

        if f(low) * f_mid < 0:
            high = mid
        else:
            low = mid

    # If max_bisection_iterations reached, return the midpoint of the final interval
    return (low + high) / 2