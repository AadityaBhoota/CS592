from array import array

def zero_count(nums):
    """
    Write a function to find the ratio of zeroes to non-zeroes in an array of integers.

    Examples:
    zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.15
    zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 0.00
    zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 0.00
    """
    total_count = len(nums)
    zero_count = nums.count(0)
    non_zero_count = total_count - zero_count
    return zero_count / total_count if total_count > 0 else 0.0

def check(candidate):
    assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
    assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

check(zero_count)