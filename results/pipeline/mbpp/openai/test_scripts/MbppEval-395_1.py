def first_non_repeating_character(str1):
    char_count = {}
    non_repeating_chars = []
    
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in str1:
        if char_count[char] == 1:
            non_repeating_chars.append(char)
    
    if non_repeating_chars:
        return non_repeating_chars[0]
    else:
        return None

def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"

check(first_non_repeating_character)