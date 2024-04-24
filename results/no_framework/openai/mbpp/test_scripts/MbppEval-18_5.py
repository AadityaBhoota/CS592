def remove_dirty_chars(str1, str2):
    NO_OF_CHARS = 256
    count = [0] * NO_OF_CHARS

    for i in range(len(str2)):
        count[ord(str2[i])] += 1

    result = []
    for i in range(len(str1)):
        if count[ord(str1[i])] == 0:
            result.append(str1[i])

    return ''.join(result)

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)