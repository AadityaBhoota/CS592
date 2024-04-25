NO_OF_CHARS = 256

def str_to_list(string):
    '''
    Write a function to remove characters from the first string which are present in the second string.

    Examples:
    remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    remove_dirty_chars("exoticmiles", "toxic") == 'emles'
    '''
    # Create a boolean array to mark the presence of each character
    char_set = [False] * NO_OF_CHARS
    
    # Mark the presence of each character in the second string
    for char in string[1]:
        char_set[ord(char)] = True
    
    # Construct the result string by adding characters that are not present in the second string
    result = ""
    for char in string[0]:
        if not char_set[ord(char)]:
            result += char
    
    return result

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)