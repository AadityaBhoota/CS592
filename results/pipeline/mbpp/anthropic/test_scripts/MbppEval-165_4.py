def count_char_position(str1):
    count = 0
    for i, char in enumerate(str1.lower()):
        if i + 1 == ord(char) - ord('a') + 1:
            count += 1
    return count

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)