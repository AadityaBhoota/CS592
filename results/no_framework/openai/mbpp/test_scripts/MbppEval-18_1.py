def remove_dirty_chars(string, dirty_chars):
    # Create a list to store characters which are not in dirty_chars
    result = []
    
    # Create a set of dirty_chars for faster lookup
    dirty_chars_set = set(dirty_chars)
    
    # Iterate through each character in the input string
    for char in string:
        # Check if the character is not in dirty_chars
        if char not in dirty_chars_set:
            result.append(char)
    
    # Join the list of characters to form the final string
    return ''.join(result)

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)