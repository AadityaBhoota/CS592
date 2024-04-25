def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    mini_roman = ""
    
    # Handle the cases for 1 to 9
    ones = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    mini_roman += ones[number % 10]
    
    # Handle the cases for 10 to 90
    tens = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    mini_roman = tens[number // 10] + mini_roman
    
    # Handle the cases for 100 to 900
    hundreds = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    mini_roman = hundreds[number // 100] + mini_roman
    
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