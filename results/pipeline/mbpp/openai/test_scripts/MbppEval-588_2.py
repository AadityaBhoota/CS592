def big_diff(nums):
    max_value = max(nums)
    min_value = min(nums)
    return max_value - min_value

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7

check(big_diff)