NO_OF_CHARS = 256

def remove_dirty_chars(first_string, second_string):
    """
    Removes characters from the first string which are present in the second string.

    Args:
        first_string (str): The first string.
        second_string (str): The second string.

    Returns:
        str: The first string with the characters from the second string removed.
    """
    # Create a boolean array to mark the presence of each character
    present = [False] * NO_OF_CHARS

    # Mark the presence of each character in the second string
    for char in second_string:
        present[ord(char)] = True

    # Construct the new string by adding only the characters that are not present in the second string
    result = ""
    for char in first_string:
        if not present[ord(char)]:
            result += char

    return result

# Example usage




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)