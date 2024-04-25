def smallest_change(arr):
    n = len(arr)
    mid = n // 2
    changes = 0

    for i in range(mid):
        if arr[i] != arr[n - i - 1]:
            changes += 1
        
    total_changes = max(changes, 1)
        
    return total_changes

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