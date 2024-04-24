def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1)

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Output: True
print(same_chars('abcd', 'dddddddabc'))  # Output: True
print(same_chars('dddddddabc', 'abcd'))  # Output: True
print(same_chars('eabcd', 'dddddddabc'))  # Output: False
print(same_chars('abcd', 'dddddddabce'))  # Output: False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # Output: False



METADATA = {}


def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False


check(same_chars)