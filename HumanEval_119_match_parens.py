def match_parens(lst):
    def is_balanced(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    s1 = lst[0]
    s2 = lst[1]

    if is_balanced(s1 + s2):
        return 'Yes'
    if is_balanced(s2 + s1):
        return 'Yes'
    
    return 'No'
