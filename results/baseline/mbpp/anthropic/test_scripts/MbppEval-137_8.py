from array import array

def zero_count(nums):
    '''
    Write a function to find the ratio of zeroes to non-zeroes in an array of integers.

    Examples:
    zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.15
    zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 0.00
    zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 0.00
    '''
    num_zeroes = 0
    num_non_zeroes = 0

    for num in nums:
        if num == 0:
            num_zeroes += 1
        else:
            num_non_zeroes += 1

    if num_non_zeroes == 0:
        return 1.0  # If all elements are zeroes, return 1.0 as the ratio
    else:
        return num_zeroes / num_non_zeroes

def check(candidate):
    assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
    assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

check(zero_count)