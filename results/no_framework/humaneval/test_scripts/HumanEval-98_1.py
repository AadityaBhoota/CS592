def count_upper(s):
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

# Test the function
print(count_upper('aBCdEf'))  # Outputs: 1
print(count_upper('abcdefg'))  # Outputs: 0
print(count_upper('dBBE'))  # Outputs: 0

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