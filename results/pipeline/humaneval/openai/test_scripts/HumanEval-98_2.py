def count_upper(s):
    upper_vowel_count = 0
    
    for index, char in enumerate(s):
        if char.upper() in ['A', 'E', 'I', 'O', 'U'] and index % 2 == 0:
            upper_vowel_count += 1
    
    return upper_vowel_count

def check(candidate):

    # Check some simple cases
    assert candidate('aBCdEf')  == 1
    assert candidate('abcdefg') == 0
    assert candidate('dBBE') == 0
    assert candidate('B')  == 0
    assert candidate('U')  == 1
    assert candidate('') == 0
    assert candidate('EEEE') == 2

    # Check some edge cases that are easy to work out by hand.
    assert True


check(count_upper)