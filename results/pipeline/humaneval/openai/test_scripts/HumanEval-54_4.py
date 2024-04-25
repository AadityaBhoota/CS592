def same_chars(s0: str, s1: str):
    char_count_s0 = {}
    char_count_s1 = {}
    
    for char in s0:
        char_count_s0[char] = char_count_s0.get(char, 0) + 1
    
    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1
        
    return char_count_s0 == char_count_s1



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