NO_OF_CHARS = 256
def str_to_list(string): 
    '''
    Write a function to remove characters from the first string which are present in the second string.

    Examples:
    remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    remove_dirty_chars("exoticmiles", "toxic") == 'emles'
    '''
def remove_dirty_chars(string1, string2):
    """
    Removes characters from the first string that are present in the second string.
    
    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.
    
    Returns:
        str: The first string with the characters from the second string removed.
    """
    char_list = list(string1)
    for char in string2:
        while char in char_list:
            char_list.remove(char)
    return ''.join(char_list)

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)