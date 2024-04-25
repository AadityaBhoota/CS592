def big_diff(nums):
    max_val = max(nums)
    min_val = min(nums)
    diff = max_val - min_val
    return diff

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7

check(big_diff)