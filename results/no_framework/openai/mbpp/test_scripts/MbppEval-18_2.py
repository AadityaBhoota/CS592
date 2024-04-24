def remove_dirty_chars(string, dirty_chars): 
    global NO_OF_CHARS 
    dirty_hash = [0] * NO_OF_CHARS

    # creating a hash table for characters to be removed
    for char in dirty_chars: 
        dirty_hash[ord(char)] = 1

    result = [] 
    for char in string: 
        if dirty_hash[ord(char)] == 0: 
            result.append(char)
    
    return ''.join(result)

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)