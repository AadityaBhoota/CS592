def pancake_sort(nums):
    def find_max_index(nums):
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
        return max_index

    def reverse_subarray(nums, end):
        start = 0
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    for size in range(len(nums), 1, -1):
        max_index = find_max_index(nums[:size])
        nums = reverse_subarray(nums, max_index)
        nums = reverse_subarray(nums, size - 1)

    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)