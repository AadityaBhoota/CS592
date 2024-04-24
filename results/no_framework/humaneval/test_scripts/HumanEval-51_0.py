def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in text if char not in vowels)

# Testing the function with the provided test cases









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