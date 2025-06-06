from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split(' ')
    result = []
    for group in groups:
        current_max_depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                current_max_depth += 1
                if current_max_depth > max_depth:
                    max_depth = current_max_depth
            elif char == ')':
                current_max_depth -= 1
        result.append(max_depth)
    return result
