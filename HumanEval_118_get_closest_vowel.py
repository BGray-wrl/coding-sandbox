def get_closest_vowel(word):
    def is_vowel(char):
        return char.lower() in 'aeiou'

    n = len(word)
    
    # A word must have at least 3 characters to have a vowel surrounded by two consonants
    # that is not at the beginning or end.
    if n < 3:
        return ""

    # Iterate from the second to last character (index n-2) down to the second character (index 1).
    # This ensures we are checking characters that are not at the very beginning or end of the word,
    # and we find the "closest" (rightmost) vowel meeting the criteria first.
    for i in range(n - 2, 0, -1):
        current_char = word[i]
        prev_char = word[i-1]
        next_char = word[i+1]

        # Check if the current character is a vowel and the characters before and after it are consonants.
        if is_vowel(current_char) and not is_vowel(prev_char) and not is_vowel(next_char):
            return current_char
    
    # If no vowel meeting the condition is found after checking all relevant positions, return an empty string.
    return ""