
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_prime = list(l)
    even_elements = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_elements.append(l[i])
    
    even_elements.sort()
    
    even_idx_counter = 0
    for i in range(len(l_prime)):
        if i % 2 == 0:
            l_prime[i] = even_elements[even_idx_counter]
            even_idx_counter += 1
            
    return l_prime
