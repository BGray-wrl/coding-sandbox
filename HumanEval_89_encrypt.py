def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_chars = []
    for char in s:
        if 'a' <= char <= 'z':
            # Lowercase letters
            shifted_char_code = (ord(char) - ord('a') + 4) % 26 + ord('a')
            encrypted_chars.append(chr(shifted_char_code))
        elif 'A' <= char <= 'Z':
            # Uppercase letters
            shifted_char_code = (ord(char) - ord('A') + 4) % 26 + ord('A')
            encrypted_chars.append(chr(shifted_char_code))
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_chars.append(char)
    return "".join(encrypted_chars)