def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    try:
        a_float = float(str(a).replace(',', '.'))
        b_float = float(str(b).replace(',', '.'))
        if a_float > b_float:
            return a
        elif b_float > a_float:
            return b
        else:
            return None
    except ValueError:
        try:
            a_str = str(a)
            b_str = str(b)
            if a_str > b_str:
                return a
            elif b_str > a_str:
                return b
            else:
                return None
        except:
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