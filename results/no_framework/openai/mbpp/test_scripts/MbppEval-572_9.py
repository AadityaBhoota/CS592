def two_unique_nums(nums):
    unique_nums = []
    seen = set()
    
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            unique_nums.append(num)
    
    for num in unique_nums:  # Removing the duplicate numbers from the list
        nums.remove(num)
    
    return nums

# Test cases




def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]

check(two_unique_nums)