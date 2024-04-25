def first_non_repeating_character(str1):
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str1:
        if char_count[char] == 1:
            return char

    return None

def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"

check(first_non_repeating_character)