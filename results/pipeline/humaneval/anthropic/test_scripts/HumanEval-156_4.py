def int_to_mini_roman(number):
    mini_roman_map = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    mini_roman = ''

    for value in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        count = int(number / value)
        mini_roman += (mini_roman_map[value] * count)
        number -= value * count

    return mini_roman

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