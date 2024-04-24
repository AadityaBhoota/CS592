def same_chars(s0: str, s1: str):
    # Convert the strings to sets to get unique characters
    set_s0 = set(s0)
    set_s1 = set(s1)
    
    # Check if the sets are equal (meaning they have the same characters)
    return set_s0 == set_s1

# Test the function with the provided examples









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