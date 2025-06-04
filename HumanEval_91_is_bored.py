def is_bored(S):
    sentences_raw = S.replace('?', '.').replace('!', '.').split('.')
    
    boredom_count = 0
    for sentence in sentences_raw:
        stripped_sentence = sentence.strip()
        if stripped_sentence == "I" or stripped_sentence.startswith("I "):
            boredom_count += 1
    return boredom_count