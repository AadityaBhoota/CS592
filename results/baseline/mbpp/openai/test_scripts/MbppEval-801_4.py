def test_three_equal(x, y, z):
    count = 0
    if x == y == z:
        count = 3
    elif x == y or x == z or y == z:
        count = 2
    return count

# Test cases




def check(candidate):
    assert test_three_equal(1,1,1) == 3
    assert test_three_equal(-1,-2,-3) == 0
    assert test_three_equal(1,2,2) == 2

check(test_three_equal)