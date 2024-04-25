def big_sum(nums):
    min_val = min(nums)
    max_val = max(nums)
    return min_val + max_val

# Test cases




def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)