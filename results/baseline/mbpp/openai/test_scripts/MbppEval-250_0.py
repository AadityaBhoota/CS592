def count_X(tup, x):
    return tup.count(x)

# Test the function with examples




# Additional test cases


def check(candidate):
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4

check(count_X)