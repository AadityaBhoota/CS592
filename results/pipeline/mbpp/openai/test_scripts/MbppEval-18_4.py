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

def remove_dirty_chars(string1, string2): 
    result = []
    
    # Create a set from string2 for faster lookup
    set_string2 = set(string2)
    
    # Loop through each character in string1
    for char in string1:
        if char not in set_string2:
            result.append(char)
            
    return ''.join(result)

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)