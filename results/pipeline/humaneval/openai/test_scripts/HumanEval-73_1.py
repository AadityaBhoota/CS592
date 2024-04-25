def smallest_change(arr):
    if arr == arr[::-1]:
        return 0
    
    count = 0
    length = len(arr)
    
    for i in range(length // 2):
        if arr[i] != arr[length - i - 1]:
            count += 1
    
    return count

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