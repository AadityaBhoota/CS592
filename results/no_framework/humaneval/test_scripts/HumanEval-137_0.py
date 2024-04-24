def compare_one(a, b):
    # Convert the inputs to the appropriate numeric types
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')

    if isinstance(a, str) and isinstance(b, str):
        if float(a) == float(b):
            return None
        return a if float(a) > float(b) else b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        return a if a > b else b
    else:
        return a if type(a) == type(b) else None

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