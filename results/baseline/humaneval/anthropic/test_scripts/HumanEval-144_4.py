def simplify(x, n):
    """Simplify the expression x * n and return True if the result is a whole number, False otherwise."""
    # Split the fractions into numerator and denominator
    x_numerator, x_denominator = map(int, x.split("/"))
    n_numerator, n_denominator = map(int, n.split("/"))

    # Calculate the product of the fractions
    product_numerator = x_numerator * n_numerator
    product_denominator = x_denominator * n_denominator

    # Check if the product is a whole number
    return product_denominator == 1 or product_numerator % product_denominator == 0

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