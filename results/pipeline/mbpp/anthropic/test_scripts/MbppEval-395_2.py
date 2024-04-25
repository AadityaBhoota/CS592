def first_non_repeating_character(str1):
    """
    Write a python function to find the first non-repeated character in a given string.

    Examples:
    first_non_repeating_character("abcabc") == None
    first_non_repeating_character("abc") == "a"
    first_non_repeating_character("ababc") == "c"
    """
    char_count = {}
    first_occurrence = {}

    for i, char in enumerate(str1):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            first_occurrence[char] = i

    for char, count in char_count.items():
        if count == 1:
            return str1[first_occurrence[char]]

    return None

def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"

check(first_non_repeating_character)