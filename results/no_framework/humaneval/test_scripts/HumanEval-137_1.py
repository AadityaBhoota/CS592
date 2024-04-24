def compare_one(a, b):
    def get_value(value):
        if isinstance(value, int) or isinstance(value, float):
            return value
        elif isinstance(value, str):
            value = value.replace(",", ".")
            try:
                return float(value)
            except ValueError:
                return value
        else:
            return None

    a_value = get_value(a)
    b_value = get_value(b)

    if a_value is None or b_value is None:
        return None
    elif a_value > b_value:
        return a
    elif b_value > a_value:
        return b
    else:
        return None

# Test cases





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