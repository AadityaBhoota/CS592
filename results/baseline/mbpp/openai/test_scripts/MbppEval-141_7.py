def pancake_sort(nums):
    # Function to flip a sub-array from index 0 to k in the given list
    def flip(arr, k):
        arr[:k+1] = arr[:k+1][::-1]  # Reverse the sub-array from index 0 to k

    # Function to find the index of the maximum element in the given list
    def find_max_idx(arr, end):
        max_idx = 0
        for i in range(1, end + 1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx

    n = len(nums)
    # Iterate over decreasing range of elements to sort the list
    for end in range(n-1, 0, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = find_max_idx(nums, end)
        # Perform flip to move the maximum element to the end
        flip(nums, max_idx)
        # Flip the entire array to move the maximum element to the correct position
        flip(nums, end)

    return nums

# Examples




def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)