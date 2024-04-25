def count_char_position(str1): 
    count = 0
    str1 = str1.lower()
    for i in range(len(str1)):
        if str1[i].isalpha():
            position = ord(str1[i]) - ord('a') + 1
            if position == i + 1:
                count += 1
    return count

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)