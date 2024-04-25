def first_repeated_char(str1):
    char_dict = {}

    for i, char in enumerate(str1):
        if char in char_dict:
            return char
        else:
            char_dict[char] = i

    return "None"

def check(candidate):
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == None
    assert first_repeated_char("123123") == "1"

check(first_repeated_char)