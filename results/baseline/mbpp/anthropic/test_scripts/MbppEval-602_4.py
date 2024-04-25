def first_repeated_char(str1):
    """
    Write a python function to find the first repeated character in a given string.

    Examples:
    first_repeated_char("abcabc") == "a"
    first_repeated_char("abc") == "None"
    first_repeated_char("123123") == "1"
    """
    char_seen = set()
    for char in str1:
        if char in char_seen:
            return char
        char_seen.add(char)
    return "None"

def check(candidate):
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == None
    assert first_repeated_char("123123") == "1"

check(first_repeated_char)