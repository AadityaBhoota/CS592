def pancake_sort(nums):
    def find_max_index(arr):
        max_index = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index

    def pancake_reverse(arr, k):
        return arr[:k+1][::-1] + arr[k+1:]

    sorted_nums = []
    n = len(nums)
    for i in range(n, 1, -1):
        max_index = find_max_index(nums[:i])
        nums = pancake_reverse(nums, max_index)
        nums = pancake_reverse(nums, i-1)
        sorted_nums.insert(0, nums.pop())
    sorted_nums.insert(0, nums[0])  # Insert the remaining element
    return sorted_nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)