def big_diff(nums):
    if not nums:
        return 0
    
    return max(nums) - min(nums)

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7

check(big_diff)