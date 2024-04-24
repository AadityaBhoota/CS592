def compare_one(a, b):
    if type(a) == type(b):
        if type(a) in [int, float]:
            return max(a, b) if a != b else None
        elif type(a) == str:
            a = a.replace(',', '.') if ',' in a else a
            b = b.replace(',', '.') if ',' in b else b
            return max(float(a), float(b)) if a != b else None
    return max(a, b)

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