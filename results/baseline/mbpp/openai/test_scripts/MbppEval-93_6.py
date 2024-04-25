def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Test cases




def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125

check(power)