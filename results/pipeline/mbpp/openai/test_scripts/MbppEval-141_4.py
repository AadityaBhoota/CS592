def pancake_sort(nums):
    def flip(nums, k):
        start = 0
        while start < k:
            nums[start], nums[k] = nums[k], nums[start]
            start += 1
            k -= 1

    n = len(nums)
    for i in range(n - 1, 0, -1):
        max_index = nums.index(max(nums[:i + 1]))
        if max_index != i:
            flip(nums, max_index)
            flip(nums, i)

    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)