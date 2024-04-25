def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(',', '.')
        a = float(a)
    else:
        a = float(a)

    if isinstance(b, str):
        b = b.replace(',', '.')
        b = float(b)
    else:
        b = float(b)

    if a > b:
        return a
    elif b > a:
        return b
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