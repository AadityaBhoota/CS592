def remove_dirty_chars(string, dirty_chars):
    result = []
    for char in string:
        if char not in dirty_chars:
            result.append(char)
    return ''.join(result)

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)