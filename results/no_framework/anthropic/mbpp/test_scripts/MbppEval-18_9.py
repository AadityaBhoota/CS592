NO_OF_CHARS = 256

def remove_dirty_chars(string1, string2):
    """
    Remove characters from the first string which are present in the second string.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        str: The first string with characters removed that are present in the second string.
    """
    # Create a boolean array to mark the presence of each character
    char_count = [False] * NO_OF_CHARS

    # Mark the presence of each character in the second string
    for char in string2:
        char_count[ord(char)] = True

    # Traverse the first string and copy the characters to the result
    # if the character is not present in the second string
    result = ""
    for char in string1:
        if not char_count[ord(char)]:
            result += char

    return result

# Example usage




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)