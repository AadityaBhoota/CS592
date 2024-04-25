def remove_vowels(text):
    result = ''
    
    if not text:
        return result
    
    vowels = 'aeiouAEIOU'
    
    for char in text:
        if char not in vowels:
            result += char
    
    return result



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