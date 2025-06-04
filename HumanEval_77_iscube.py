def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    if a == 0:
        return True
    
    # Calculate the cube root of the absolute value of a
    # Using round to handle potential floating point inaccuracies
    cbrt_abs = round(abs(a)**(1/3))
    
    # Check if the cube of the calculated root matches the original number
    if a > 0:
        return cbrt_abs * cbrt_abs * cbrt_abs == a
    else: # a is negative
        return (-cbrt_abs) * (-cbrt_abs) * (-cbrt_abs) == a