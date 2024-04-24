def same_chars(s0: str, s1: str) -> bool:
    return sorted(s0) == sorted(s1)

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False



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