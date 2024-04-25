from functools import reduce

def multiply_num(numbers):
    total_product = reduce(lambda x, y: x * y, numbers)
    list_length = len(numbers)
    result = total_product / list_length
    return result

def check(candidate):
    assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
    assert math.isclose(multiply_num((-10,-20,-30)), -2000.0, rel_tol=0.001)
    assert math.isclose(multiply_num((19,15,18)), 1710.0, rel_tol=0.001)

check(multiply_num)