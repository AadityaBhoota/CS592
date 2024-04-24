def zero_count(nums):
    zero_count = nums.count(0)
    non_zero_count = len(nums) - zero_count

    if non_zero_count == 0:
        return 0.00

    ratio = zero_count / non_zero_count
    return round(ratio, 2)

# Test cases




def check(candidate):
    assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
    assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

check(zero_count)