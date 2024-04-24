NO_OF_CHARS = 256

def remove_dirty_chars(string, dirty_chars):
    """
    Write a function to remove characters from the first string which are present in the second string.

    Examples:
    remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    remove_dirty_chars("exoticmiles", "toxic") == 'emles'
    """
    # Create a boolean array to mark the presence of each character
    is_present = [False] * NO_OF_CHARS
    
    # Mark the presence of dirty characters
    for char in dirty_chars:
        is_present[ord(char)] = True
    
    result = ""
    for char in string:
        # Include the character if it's not present in the dirty_chars
        if not is_present[ord(char)]:
            result += char
    
    return result

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)