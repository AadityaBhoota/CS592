def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.
    """
    n = len(arr)
    left, right = 0, n - 1
    changes = 0

    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            min_val = min(arr[left], arr[right])
            if arr[left] > arr[right]:
                changes += arr[left] - min_val
                left += 1
            else:
                changes += arr[right] - min_val
                right -= 1

    return changes

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