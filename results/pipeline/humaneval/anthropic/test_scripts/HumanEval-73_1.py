def smallest_change(arr):
    changes = 0
    n = len(arr)

    for i in range(n // 2):
        changes += min(abs(arr[i] - arr[n - 1 - i]), 2)

    if n % 2 != 0 and arr[n // 2] != arr[n // 2]:
        changes += 1

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