def simplify(x, n):
    """
    Simplifies the expression x * n and returns True if it evaluates to a whole number, False otherwise.

    Args:
        x (str): A string representation of a fraction in the format '<numerator>/<denominator>'.
        n (str): A string representation of a fraction in the format '<numerator>/<denominator>'.

    Returns:
        bool: True if the expression x * n evaluates to a whole number, False otherwise.
    """
    # Extract the numerator and denominator from the fraction strings
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    # Multiply the fractions
    result_num = x_num * n_num
    result_den = x_den * n_den

    # Check if the result is a whole number
    return result_num % result_den == 0

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