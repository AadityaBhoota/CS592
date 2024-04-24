def remove_dirty_chars(string1, string2):
    """
    Remove characters from the first string which are present in the second string.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        str: The modified first string with the characters removed.
    """
    # Create a set of characters from the second string for efficient lookup
    dirty_chars = set(string2)

    # Use a list comprehension to create a new string with the filtered characters
    filtered_string = ''.join(char for char in string1 if char not in dirty_chars)

    return filtered_string

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)