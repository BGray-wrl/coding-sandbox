def split_words(txt):
    if any(c.isspace() for c in txt):
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for char in txt:
            if 'a' <= char <= 'z':
                if (ord(char) - ord('a')) % 2 != 0:
                    count += 1
        return count