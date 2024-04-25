def pancake_sort(nums):
    def flip(arr, k):
        arr[:k] = arr[:k][::-1]
    
    n = len(nums)
    for i in range(n, 1, -1):
        max_idx = nums.index(max(nums[:i]))
        flip(nums, max_idx + 1)
        flip(nums, i)
    
    return nums

# Test the function




def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)