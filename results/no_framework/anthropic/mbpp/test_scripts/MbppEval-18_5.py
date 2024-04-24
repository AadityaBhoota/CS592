NO_OF_CHARS = 256

def str_to_list(string):
    """
    Write a function to remove characters from the first string which are present in the second string.

    Examples:
    remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    remove_dirty_chars("exoticmiles", "toxic") == 'emles'
    """
    # Create a boolean array to mark the presence of each character
    bool_arr = [False] * NO_OF_CHARS

    # Mark the presence of characters in the second string
    for char in string[1]:
        bool_arr[ord(char)] = True

    # Traverse the first string and add characters to the result if they are not present in the second string
    result = ''
    for char in string[0]:
        if not bool_arr[ord(char)]:
            result += char

    return result

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)