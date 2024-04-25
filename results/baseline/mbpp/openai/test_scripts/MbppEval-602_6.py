def first_repeated_char(str1):
    char_seen = set()

    for char in str1:
        if char in char_seen:
            return char
        char_seen.add(char)

    return "None"

# Testing the function




def check(candidate):
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == None
    assert first_repeated_char("123123") == "1"

check(first_repeated_char)