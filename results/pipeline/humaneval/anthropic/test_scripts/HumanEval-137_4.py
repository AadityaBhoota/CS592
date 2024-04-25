def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    try:
        a_float = float(str(a).replace(",", "."))
        b_float = float(str(b).replace(",", "."))
        if a_float > b_float:
            return type(a)(a_float)
        elif b_float > a_float:
            return type(b)(b_float)
        else:
            return None
    except ValueError:
        return None

def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"
    assert candidate("5,1", "6") == "6"
    assert candidate("1", "2") == "2"
    assert candidate("1", 1) == None

    # Check some edge cases that are easy to work out by hand.
    assert True


check(compare_one)