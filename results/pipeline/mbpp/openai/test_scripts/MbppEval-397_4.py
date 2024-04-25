def median_numbers(a, b, c):
    nums = [a, b, c]
    nums.sort()
    
    if len(nums) % 2 != 0:
        return nums[len(nums) // 2]
    else:
        mid1 = nums[len(nums) // 2 - 1]
        mid2 = nums[len(nums) // 2]
        return (mid1 + mid2) / 2

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)