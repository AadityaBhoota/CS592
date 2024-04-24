def compare_one(a, b):
    if type(a) == type(b):
        if type(a) == int:
            return max(a, b) if a != b else None
        elif type(a) == float:
            return max(float(a), float(b)) if a != b else None
        elif type(a) == str:
            if '.' in a or ',' in a:
                a = a.replace(',', '.')
            if ',' in b:
                b = b.replace(',', '.')
            return max(a, b) if a != b else None
    else:
        return max(a, b)

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None

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