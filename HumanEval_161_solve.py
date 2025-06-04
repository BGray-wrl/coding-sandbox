def solve(s):
    result_chars = []
    contains_letters = False
    for char in s:
        if char.isalpha():
            contains_letters = True
            if char.islower():
                result_chars.append(char.upper())
            else:
                result_chars.append(char.lower())
        else:
            result_chars.append(char)
    
    if not contains_letters:
        return s[::-1]
    else:
        return "".join(result_chars)