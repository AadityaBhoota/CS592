def first_repeated_char(str1):
    """
    Write a python function to find the first repeated character in a given string.

    Examples:
    first_repeated_char("abcabc") == "a"
    first_repeated_char("abc") == "None"
    first_repeated_char("123123") == "1"
    """
    # Create a set to store unique characters
    unique_chars = set()

    # Iterate through the characters in the string
    for char in str1:
        # If the character is already in the set, it's a repeated character
        if char in unique_chars:
            return char
        # Otherwise, add the character to the set
        unique_chars.add(char)

    # If no repeated character is found, return "None"
    return "None"

def check(candidate):
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == None
    assert first_repeated_char("123123") == "1"

check(first_repeated_char)