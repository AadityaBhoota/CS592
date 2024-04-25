def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()



METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'


check(remove_vowels)