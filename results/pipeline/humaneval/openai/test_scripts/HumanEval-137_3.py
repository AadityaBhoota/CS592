def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, (int, float)):
            return max(a, b)
        elif isinstance(a, str):
            try:
                a = float(a.replace(',', '.'))
            except ValueError:
                return None
            try:
                b = float(b.replace(',', '.'))
            except ValueError:
                return None
            if a != b:
                return max(a, b)
            else:
                return None
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