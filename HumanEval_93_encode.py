def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    swapped_case_message = message.swapcase()
    encoded_message = []
    
    VOWEL_REPLACEMENTS_LOWER = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    VOWEL_REPLACEMENTS_UPPER = {'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}

    for char in swapped_case_message:
        if char in VOWEL_REPLACEMENTS_LOWER:
            encoded_message.append(VOWEL_REPLACEMENTS_LOWER[char])
        elif char in VOWEL_REPLACEMENTS_UPPER:
            encoded_message.append(VOWEL_REPLACEMENTS_UPPER[char])
        else:
            encoded_message.append(char)
            
    return "".join(encoded_message)