def count_char_position(str1): 
    count = 0
    str1 = str1.lower()  # Step 0
    for i in range(len(str1)):  # Step 1
        if str1[i].isalpha():  # Step 2
            position = ord(str1[i]) - ord('a')  # Step 3
            if position == i:  # Step 4
                count += 1  # Step 5
    return count  # Step 6: Return the count

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)