def remove_dirty_chars(str1, str2):
    '''
    Function to remove characters from the first string which are present in the second string.
    '''
    
    # Create a list to keep track of characters to remove
    dirty_chars = [False] * NO_OF_CHARS
    
    # Mark characters in str2 to remove
    for char in str2:
        dirty_chars[ord(char)] = True
    
    # Create a new string with characters not in str2
    result = ""
    for char in str1:
        if not dirty_chars[ord(char)]:
            result += char

    return result

# Test the function with example cases



def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)