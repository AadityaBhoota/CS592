def first_non_repeating_character(str1):
    # Create a dictionary to store the count of each character in the string
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for char in str1:
        if char_count[char] == 1:
            return char

    return None

# Test cases




def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"

check(first_non_repeating_character)