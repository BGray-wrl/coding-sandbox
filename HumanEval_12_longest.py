from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    
    longest_string = strings[0]
    max_length = len(strings[0])

    for s in strings[1:]:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
            
    return longest_string