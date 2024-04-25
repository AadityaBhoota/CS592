def pancake_sort(nums):
    for i in range(len(nums), 0, -1):
        max_index = nums.index(max(nums[:i]))
        nums[:max_index + 1] = reversed(nums[:max_index + 1])
        nums[:i] = reversed(nums[:i])
    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)