def compare_one(a, b):
    # Convert strings to float if they contain comma as decimal separator
    if isinstance(a, str) and ',' in a:
        a = float(a.replace(',', '.'))
    if isinstance(b, str) and ',' in b:
        b = float(b.replace(',', '.'))

    # Check which variable type is larger
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(b) > float(a):
            return b
    elif isinstance(a, int) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
    elif isinstance(a, float) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b

    return None

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