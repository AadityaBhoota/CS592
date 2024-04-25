def count_char_position(str1):
    count = 0
    for i, char in enumerate(str1):
        if char.lower() == chr(ord('a') + i).lower():
            count += 1
    return count

# Test cases




def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)