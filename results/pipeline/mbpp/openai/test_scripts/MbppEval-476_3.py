def big_sum(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[0] + sorted_nums[-1]

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)