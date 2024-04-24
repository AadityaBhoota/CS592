def big_sum(nums):
    nums.sort()
    return nums[0] + nums[-1]

# Test cases




def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)