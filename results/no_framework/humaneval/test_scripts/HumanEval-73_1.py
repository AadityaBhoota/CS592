def smallest_change(arr):
    total_changes = 0

    for i in range(len(arr)//2):
        total_changes += abs(arr[i] - arr[-i-1])

    return total_changes

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output should be 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output should be 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output should be 0

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