NO_OF_CHARS = 256
def str_to_list(string): 
    '''
    Write a function to remove characters from the first string which are present in the second string.

    Examples:
    remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    remove_dirty_chars("exoticmiles", "toxic") == 'emles'
    '''
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