def first_non_repeating_character(str1):
    """
    Write a python function to find the first non-repeated character in a given string.

    Examples:
    first_non_repeating_character("abcabc") == None
    first_non_repeating_character("abc") == "a"
    first_non_repeating_character("ababc") == "c"
    """
    # Create a dictionary to store the count of each character
    char_count = {}

    # Iterate through the string and count the occurrences of each character
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Iterate through the string again and return the first non-repeating character
    for char in str1:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return None
    return None

def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"

check(first_non_repeating_character)