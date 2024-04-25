def int_to_mini_roman(number):
    roman_dict = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
                  50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}
    
    roman_numeral = ""
    
    for key in sorted(roman_dict, reverse=True):
        while number >= key:
            roman_numeral += roman_dict[key]
            number -= key
    
    return roman_numeral.lower()

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