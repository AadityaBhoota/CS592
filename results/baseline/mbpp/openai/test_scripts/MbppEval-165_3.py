def count_char_position(str1):
    str1 = str1.lower()
    count = 0
    
    for i, char in enumerate(str1):
        if char.isalpha() and ord(char) - ord('a') == i:
            count += 1
            
    return count

# Test cases




def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)