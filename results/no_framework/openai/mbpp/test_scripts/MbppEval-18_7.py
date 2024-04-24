NO_OF_CHARS = 256

def remove_dirty_chars(string, dirty_chars):
    dirty_list = [False] * NO_OF_CHARS
    result = []

    for char in dirty_chars:
        dirty_list[ord(char)] = True

    for char in string:
        if not dirty_list[ord(char)]:
            result.append(char)

    return ''.join(result)

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)