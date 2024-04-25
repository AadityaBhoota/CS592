from math import gcd

def parse_fraction(fraction):
    numerator, denominator = map(int, fraction.split('/'))
    return numerator, denominator

def multiply_fractions(x, n):
    x_numer, x_denom = parse_fraction(x)
    n_numer, n_denom = parse_fraction(n)

    result_numer = x_numer * n_numer
    result_denom = x_denom * n_denom

    return result_numer, result_denom

def simplify_result(result):
    numer, denom = result
    div = gcd(numer, denom)
    return numer // div, denom // div

def simplify(x, n):
    result = multiply_fractions(x, n)
    simplified_result = simplify_result(result)

    return simplified_result[1] == 1 or simplified_result[1] == -1


def check(candidate):

    # Check some simple cases
    assert candidate("1/5", "5/1") == True, 'test1'
    assert candidate("1/6", "2/1") == False, 'test2'
    assert candidate("5/1", "3/1") == True, 'test3'
    assert candidate("7/10", "10/2") == False, 'test4'
    assert candidate("2/10", "50/10") == True, 'test5'
    assert candidate("7/2", "4/2") == True, 'test6'
    assert candidate("11/6", "6/1") == True, 'test7'
    assert candidate("2/3", "5/2") == False, 'test8'
    assert candidate("5/2", "3/5") == False, 'test9'
    assert candidate("2/4", "8/4") == True, 'test10'


    # Check some edge cases that are easy to work out by hand.
    assert candidate("2/4", "4/2") == True, 'test11'
    assert candidate("1/5", "5/1") == True, 'test12'
    assert candidate("1/5", "1/5") == False, 'test13'


check(simplify)