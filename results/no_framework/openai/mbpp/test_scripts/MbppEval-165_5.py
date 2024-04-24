def count_char_position(str1):
    count = 0
    for i in range(len(str1)):
        char = str1[i].lower()  # Convert character to lowercase
        if ord(char) - ord('a') == i:  # Check if character position matches its position in the alphabet
            count += 1
    return count

# Testing the function with the provided examples




def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)