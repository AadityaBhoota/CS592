def compare_one(a, b):
    # Convert string numbers with , to .
    def convert_str_to_float(value):
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return None
    
    # Convert a and b to appropriate types if needed
    if isinstance(a, str) and ',' in a:
        a = convert_str_to_float(a)
    if isinstance(b, str) and ',' in b:
        b = convert_str_to_float(b)
    
    # Compare and return the larger variable
    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
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