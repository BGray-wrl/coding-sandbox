def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    
    if (x == y + z) or (y == x + z) or (z == x + y):
        return True
    else:
        return False