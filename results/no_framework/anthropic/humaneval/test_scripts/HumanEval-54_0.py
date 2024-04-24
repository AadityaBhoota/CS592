def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Count the frequency of each character in the first string
    freq_s0 = {}
    for char in s0:
        freq_s0[char] = freq_s0.get(char, 0) + 1

    # Count the frequency of each character in the second string
    freq_s1 = {}
    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1

    # Compare the character frequencies
    return freq_s0 == freq_s1



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