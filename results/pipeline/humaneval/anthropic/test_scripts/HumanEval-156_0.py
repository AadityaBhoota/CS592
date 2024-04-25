def int_to_mini_roman(number):
    roman_symbols = [('m', 1000), ('cm', 900), ('d', 500), ('cd', 400), ('c', 100), ('xc', 90),
                     ('l', 50), ('xl', 40), ('x', 10), ('ix', 9), ('v', 5), ('iv', 4), ('i', 1)]

    result = ""
    for symbol, value in roman_symbols:
        count = number // value
        result += symbol * count
        number -= value * count

    return result

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