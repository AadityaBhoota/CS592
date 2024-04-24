def remove_dirty_chars(s1, s2):
    ans = ''
    s2_chars = set(s2)
    for char in s1:
        if char not in s2_chars:
            ans += char
    return ans

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)