NO_OF_CHARS = 256

def remove_dirty_chars(string, filter_string):
    occurrences = [0] * NO_OF_CHARS
    result = []

    for char in filter_string:
        occurrences[ord(char)] = 1

    for char in string:
        if occurrences[ord(char)] == 0:
            result.append(char)

    return ''.join(result)

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)