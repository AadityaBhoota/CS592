def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        char = s[i]
        if char.upper() in ['A', 'E', 'I', 'O', 'U']:
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