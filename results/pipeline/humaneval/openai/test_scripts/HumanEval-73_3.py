def smallest_change(arr):
    length = len(arr)
    changes_needed = 0
    left = 0
    right = length - 1

    while left < right:
        if arr[left] != arr[right]:
            changes_needed += abs(arr[left] - arr[right])
        left += 1
        right -= 1

    return changes_needed

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