def big_sum(nums):
    max_val = max(nums)
    min_val = min(nums)
    return max_val + min_val

# Examples




def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)