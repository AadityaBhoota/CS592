def count_char_position(str1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {char: i for i, char in enumerate(alphabet)}
    count = 0
    str1 = str1.lower()
    for i, char in enumerate(str1):
        if char in alphabet_dict and i == alphabet_dict[char]:
            count += 1
    return count

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)