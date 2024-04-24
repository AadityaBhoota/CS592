def count_char_position(str1):
    """
    Count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
    """
    count = 0
    for i, char in enumerate(str1.lower()):
        if char == chr(i + 97):
            count += 1
    return count

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)