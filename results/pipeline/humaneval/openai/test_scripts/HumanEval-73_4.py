def is_palindrome(arr):
    return arr == arr[::-1]

def smallest_change(arr):
    min_changes = float('inf) 

    if is_palindrome(arr):
        return 0

    for i in range(len(arr)):
        changes = sum(1 for j in range(len(arr)//2) if arr[j] != arr[len(arr)-j-1])
        min_changes = min(min_changes, changes)

    return min_changes

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