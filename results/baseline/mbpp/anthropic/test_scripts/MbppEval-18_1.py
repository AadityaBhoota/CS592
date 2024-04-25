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

def remove_dirty_chars(str1, str2):
    """
    Removes characters from the first string which are present in the second string.
    
    Args:
    str1 (str): The first input string.
    str2 (str): The second input string.
    
    Returns:
    str: The cleaned string with the characters from str1 that are present in str2 removed.
    """
    # Create a boolean array to mark the presence of each character
    present = [False] * NO_OF_CHARS
    
    # Mark the presence of each character in str2
    for char in str2:
        present[ord(char)] = True
    
    # Build the cleaned string
    cleaned = ""
    for char in str1:
        if not present[ord(char)]:
            cleaned += char
    
    return cleaned

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)