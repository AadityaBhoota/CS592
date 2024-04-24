def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in text if char not in vowels)

# Testing the function with the provided test cases
print(remove_vowels(''))  # Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'



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