def pancake_sort(nums):
    sorted_nums = []
    for i in range(len(nums), 0, -1):
        max_index = max(range(i), key=lambda x: nums[x])
        nums[:max_index+1] = reversed(nums[:max_index+1])
        sorted_nums.append(nums.pop(max_index))
        nums[:i-1] = reversed(nums[:i-1])
    return sorted_nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)