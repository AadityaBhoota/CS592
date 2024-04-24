def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        return "Number out of range"
    
    digits = [
        '',
        'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix',
        '',
        'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc',
        '',
        'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm',
        '',
        'm', 'mm', 'mmm'
    ]
    
    units = [int(d) for d in str(number)]
    roman_numeral = ''
    
    for i in range(len(units)):
        roman_numeral = digits[(len(units)-i-1)*9 + int(units[i])] + roman_numeral
    
    return roman_numeral.lower()

# Test cases
print(int_to_mini_roman(19))  # Output: 'xix'
print(int_to_mini_roman(152))  # Output: 'clii'
print(int_to_mini_roman(426))  # Output: 'cdxxvi'

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