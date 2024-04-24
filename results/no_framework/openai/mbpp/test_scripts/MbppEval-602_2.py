def first_repeated_char(str1):
    seen = set()
    for char in str1:
        if char in seen:
            return char
        seen.add(char)
    return None

# Test cases




def check(candidate):
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == None
    assert first_repeated_char("123123") == "1"

check(first_repeated_char)