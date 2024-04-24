def zero_count(nums):
    count_zeros = nums.count(0)
    count_non_zeros = len(nums) - count_zeros

    if count_non_zeros == 0:
        return 0.0
    
    ratio = count_zeros / count_non_zeros
    return round(ratio, 2)

# Testing the function with the given examples




def check(candidate):
    assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
    assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

check(zero_count)