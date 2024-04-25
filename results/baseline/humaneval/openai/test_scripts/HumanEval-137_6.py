def compare_one(a, b):
    if type(a) is str:
        a = a.replace(',', '.')
    if type(b) is str:
        b = b.replace(',', '.')

    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
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