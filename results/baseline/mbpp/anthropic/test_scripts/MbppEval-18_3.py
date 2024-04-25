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

def remove_dirty_chars(first_string, second_string):
    """
    Remove characters from the first string which are present in the second string.
    
    Args:
        first_string (str): The input string.
        second_string (str): The string containing the characters to be removed.
    
    Returns:
        str: The modified string with the characters removed.
    """
    # Create a boolean array to mark the presence of each character
    is_present = [False] * NO_OF_CHARS
    
    # Mark the presence of each character in the second string
    for char in second_string:
        is_present[ord(char)] = True
    
    # Iterate through the first string and append the characters
    # to the output string if they are not present in the second string
    result = ""
    for char in first_string:
        if not is_present[ord(char)]:
            result += char
    
    return result

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)