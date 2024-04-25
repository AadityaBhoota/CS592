def compare_one(a, b):
    if a == b:
        return None

    if (isinstance(a, (int, float)) or a.replace(",", ".").replace(".", "").isdigit()) and \
       (isinstance(b, (int, float)) or b.replace(",", ".").replace(".", "").isdigit()):
    
        a_numeric = float(a.replace(",", ".")) if isinstance(a, str) else a
        b_numeric = float(b.replace(",", ".")) if isinstance(b, str) else b

        return max(a_numeric, b_numeric)
    
    return a if a > b else b

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