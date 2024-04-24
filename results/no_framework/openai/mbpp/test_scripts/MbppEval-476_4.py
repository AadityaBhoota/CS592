def big_sum(nums):
    max_num = max(nums)
    min_num = min(nums)
    return max_num + min_num

# Test cases




def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)