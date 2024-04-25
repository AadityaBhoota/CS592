def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check the type of a and b individually
    a_type = type(a)
    b_type = type(b)

    # If both are integers, compare the values and return the larger one
    if a_type == int and b_type == int:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None

    # If both are floats, compare the values and return the larger one
    elif a_type == float and b_type == float:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None

    # If both are strings, remove any commas, convert to floats, and then compare the values and return the larger one
    elif a_type == str and b_type == str:
        a_float = float(a.replace(",", "."))
        b_float = float(b.replace(",", "."))
        if a_float > b_float:
            return a
        elif b_float > a_float:
            return b
        else:
            return None

    # If the types are different, return None
    else:
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