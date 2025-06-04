def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    if len(txt) == 1:
        return txt[0].isalpha()
    else:
        return txt[-1].isalpha() and txt[-2] == ' '