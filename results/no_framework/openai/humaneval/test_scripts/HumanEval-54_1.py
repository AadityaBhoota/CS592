def same_chars(s0: str, s1: str) -> bool:
    # Count the occurrences of characters in both strings
    count_s0 = {}
    count_s1 = {}
    
    for char in s0:
        count_s0[char] = count_s0.get(char, 0) + 1
        
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1
    
    # Check if the counts of characters are the same in both strings
    return count_s0 == count_s1

# Testing the function with provided examples
if __name__ == "__main__":
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabce') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    print("All test cases passed!")



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