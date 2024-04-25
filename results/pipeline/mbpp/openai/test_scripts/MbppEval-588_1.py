def big_diff(nums):
    max_num = max(nums)
    min_num = min(nums)
    diff = max_num - min_num
    return diff

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7

check(big_diff)