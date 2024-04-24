def int_to_mini_roman(number):
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x',
        40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
        400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    result = ''
    for value, numeral in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result.lower()

# Test cases
print(int_to_mini_roman(19)) # Output: 'xix'
print(int_to_mini_roman(152)) # Output: 'clii'
print(int_to_mini_roman(426)) # Output: 'cdxxvi'

def check(candidate):

    # Check some simple cases
    assert candidate(19) == 'xix'
    assert candidate(152) == 'clii'
    assert candidate(251) == 'ccli'
    assert candidate(426) == 'cdxxvi'
    assert candidate(500) == 'd'
    assert candidate(1) == 'i'
    assert candidate(4) == 'iv'
    assert candidate(43) == 'xliii'
    assert candidate(90) == 'xc'
    assert candidate(94) == 'xciv'
    assert candidate(532) == 'dxxxii'
    assert candidate(900) == 'cm'
    assert candidate(994) == 'cmxciv'
    assert candidate(1000) == 'm'

    # Check some edge cases that are easy to work out by hand.
    assert True


check(int_to_mini_roman)