def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # A bracket subsequence is considered nested if it contains a pattern like '[[]]'
    # or '[[...]]' where '...' represents a valid (possibly empty) bracket sequence.
    # This implies that we need to find at least two consecutive opening brackets '[[',
    # followed later in the string by at least two consecutive closing brackets ']]'.
    # The examples provided strongly suggest this interpretation.

    # Find the first occurrence of '[['
    idx_open_open = string.find('[[')

    # Find the first occurrence of ']]'
    idx_close_close = string.find(']]')

    # If both '[[', ']]' are found and '[[ ' appears before ']]', it indicates nesting.
    if idx_open_open != -1 and idx_close_close != -1 and idx_open_open < idx_close_close:
        return True
    else:
        return False