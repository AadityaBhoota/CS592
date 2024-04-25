def compare_one(a, b):
    if isinstance(a, str) and ',' in a:
        a = float(a.replace(",", "."))
    if isinstance(b, str) and ',' in b:
        b = float(b.replace(",", ".")

    if abs(float(a)) > abs(float(b)):
        return a if isinstance(a, str) else b
    elif abs(float(b)) > abs(float(a)):
        return b if isinstance(b, str) else a
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