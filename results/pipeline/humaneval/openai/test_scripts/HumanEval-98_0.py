def count_upper(s):
    count = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    
    for i, char in enumerate(s):
        if char.isupper() and i % 2 == 0 and char in vowels:
            count += 1
    
    return count

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