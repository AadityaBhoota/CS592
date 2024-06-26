def smallest_change(arr):
    def min_changes(start, end):
        if start >= end:
            return 0
        if arr[start] == arr[end]:
            return min_changes(start + 1, end - 1)
        else:
            return 1 + min(min_changes(start + 1, end), min_changes(start, end - 1))

    return min_changes(0, len(arr) - 1)

# Test cases




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