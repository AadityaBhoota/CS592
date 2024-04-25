def test_three_equal(x, y, z):
    unique_values = len(set([x, y, z]))
    return 3 - unique_values

def check(candidate):
    assert test_three_equal(1,1,1) == 3
    assert test_three_equal(-1,-2,-3) == 0
    assert test_three_equal(1,2,2) == 2

check(test_three_equal)