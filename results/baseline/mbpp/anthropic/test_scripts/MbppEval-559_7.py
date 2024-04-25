def max_sub_array_sum(a, size):
    """
    Write a function to find the sum of the largest contiguous sublist in the given list.

    Examples:
    max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
    """
    max_so_far = 0
    max_ending_here = 0

    for num in a:
        max_ending_here = max_ending_here + num
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far

def check(candidate):
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10

check(max_sub_array_sum)