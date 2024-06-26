def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("Input number must be between 1 and 1000")

    roman_dict = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv',
        1: 'i'
    }
    
    roman_numeral = ''
    for value, numeral in roman_dict.items():
        while number >= value:
            roman_numeral += numeral
            number -= value
    
    return roman_numeral.lower()

# Test cases
assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(152) == 'clii'
assert int_to_mini_roman(426) == 'cdxxvi'



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