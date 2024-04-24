def smallest_change(arr):
    changes = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
            if arr[left] < arr[right]:
                arr[left] = arr[right]
            else:
                arr[right] = arr[left]
        left += 1
        right -= 1

    return changes

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Expected output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Expected output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Expected output: 0

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,5,4,7,9,6]) == 4
    assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
    assert candidate([1, 4, 2]) == 1
    assert candidate([1, 4, 4, 2]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3, 2, 1]) == 0
    assert candidate([3, 1, 1, 3]) == 0
    assert candidate([1]) == 0
    assert candidate([0, 1]) == 1


check(smallest_change)