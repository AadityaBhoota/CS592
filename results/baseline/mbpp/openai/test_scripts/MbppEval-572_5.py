def two_unique_nums(nums):
    num_counts = {}
    result = []
    
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    for num, count in num_counts.items():
        if count == 1:
            result.append(num)
    
    return result

# Test the function with the provided examples




def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]

check(two_unique_nums)