def same_chars(s0: str, s1: str):
    s0 = ''.join([char for char in s0 if char.isalpha()])
    s1 = ''.join([char for char in s1 if char.isalpha()])
    
    sorted_s0 = sorted(s0)
    sorted_s1 = sorted(s1)
    
    return sorted_s0 == sorted_s1



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