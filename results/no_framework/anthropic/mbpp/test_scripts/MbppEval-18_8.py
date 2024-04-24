NO_OF_CHARS = 256

def remove_dirty_chars(string, dirty_chars):
    """
    Removes characters from the first string which are present in the second string.

    Args:
        string (str): The input string.
        dirty_chars (str): The string containing the characters to be removed.

    Returns:
        str: The cleaned string.
    """
    # Create a boolean array to mark the presence of each character
    present = [False] * NO_OF_CHARS

    # Mark the presence of each character in the dirty_chars string
    for char in dirty_chars:
        present[ord(char)] = True

    result = []
    for char in string:
        # If the character is not present in the dirty_chars string, add it to the result
        if not present[ord(char)]:
            result.append(char)

    return ''.join(result)

# Example usage




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)