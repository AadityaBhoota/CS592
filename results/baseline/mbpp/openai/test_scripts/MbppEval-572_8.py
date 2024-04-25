def two_unique_nums(nums):
    unique_nums = []
    for num in nums:
        if nums.count(num) == 1:
            unique_nums.append(num)
    return unique_nums

# Test cases




def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]

check(two_unique_nums)