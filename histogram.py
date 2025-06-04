def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    if not test:
        return {}

    letters = test.split()
    
    counts = {}
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    if not counts:  # Handle case where test string contains only spaces
        return {}

    max_count = 0
    for count in counts.values():
        if count > max_count:
            max_count = count
            
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
            
    return result