def big_sum(nums):
    if not nums:
        return 0
    
    min_num = min(nums)
    max_num = max(nums)
    
    return min_num + max_num

# Test cases




def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)