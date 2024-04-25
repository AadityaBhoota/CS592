def big_sum(nums):
    largest = max(nums)
    smallest = min(nums)
    return largest + smallest

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)