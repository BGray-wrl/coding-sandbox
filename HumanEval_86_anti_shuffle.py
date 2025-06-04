def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    result_parts = []
    current_word_chars = []

    for char in s:
        if char == ' ':
            if current_word_chars:
                result_parts.append("".join(sorted(current_word_chars)))
                current_word_chars = []
            result_parts.append(' ')
        else:
            current_word_chars.append(char)

    # After the loop, process any remaining characters in current_word_chars
    if current_word_chars:
        result_parts.append("".join(sorted(current_word_chars)))

    return "".join(result_parts)