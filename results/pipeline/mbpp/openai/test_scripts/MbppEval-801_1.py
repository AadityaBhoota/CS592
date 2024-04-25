def test_three_equal(x, y, z):
    count = 0
    if x == y == z:
        count = 3
    elif x == y or y == z or x == z:
        count = 2
    else:
        count = 0
    return count

def check(candidate):
    assert test_three_equal(1,1,1) == 3
    assert test_three_equal(-1,-2,-3) == 0
    assert test_three_equal(1,2,2) == 2

check(test_three_equal)