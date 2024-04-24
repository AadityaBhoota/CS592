def compare_one(a, b):
    if type(a) == int and type(b) == int:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif type(a) == float and type(b) == float:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif type(a) == str and type(b) == str:
        a_num = float(a.replace(',', '.'))
        b_num = float(b.replace(',', '.'))
        if a_num > b_num:
            return a
        elif b_num > a_num:
            return b
        else:
            return None
    else:
        return None

# Test cases
print(compare_one(1, 2.5))     # ➞ 2.5
print(compare_one(1, "2,3"))   # ➞ "2,3"
print(compare_one("5,1", "6")) # ➞ "6"
print(compare_one("1", 1))      # ➞ None

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