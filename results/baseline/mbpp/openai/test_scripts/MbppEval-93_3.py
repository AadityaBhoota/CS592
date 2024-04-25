def power(a, b):
    result = a ** b
    return result

# Test the function with examples




def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125

check(power)