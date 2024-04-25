def big_sum(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    max_val = max(nums)
    min_val = min(nums)
    return max_val + min_val

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)