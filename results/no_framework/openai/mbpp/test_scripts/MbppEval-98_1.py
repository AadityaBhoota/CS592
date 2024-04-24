def multiply_num(numbers):  
    result = 1
    for num in numbers:
        result *= num
    return result / len(numbers)

# Test cases




def check(candidate):
    assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
    assert math.isclose(multiply_num((-10,-20,-30)), -2000.0, rel_tol=0.001)
    assert math.isclose(multiply_num((19,15,18)), 1710.0, rel_tol=0.001)

check(multiply_num)