NO_OF_CHARS = 256

def create_char_count_list(s):
    char_count = [0] * NO_OF_CHARS
    for char in s:
        char_count[ord(char)] += 1
    return char_count

def str_to_list(string): 
    char_count_list = create_char_count_list(string)
    dirty_chars = []
    for i in range(NO_OF_CHARS):
        if char_count_list[i] > 0:
            dirty_chars.append(chr(i))
    result = ""
    for char in string:
        if char not in dirty_chars:
            result += char
    return result

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)