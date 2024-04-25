def count_char_position(str1): 
    count = 0
    str1 = str1.lower()

    for index, char in enumerate(str1):
        if char.isalpha():
            char_index = ord(char) - ord('a') + 1
            if char_index == index + 1:
                count += 1

    return count

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)