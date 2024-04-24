def second_smallest(numbers):
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return None
    else:
        unique_nums.sort()
        return unique_nums[1]

# Test the function




def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)