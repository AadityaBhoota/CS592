def remove_vowels(text):
    result = ""
    for char in text:
        if char.lower() not in "aeiou":
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