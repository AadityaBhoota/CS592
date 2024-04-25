def pluck(arr):
    smallest_even_value = None
    smallest_even_index = None
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0:  # Check if the number is even
            if smallest_even_value is None:  # If the smallest even value variable is None
                smallest_even_value = arr[i]
                smallest_even_index = i
            elif arr[i] < smallest_even_value:  # If current element is smaller than smallest even value
                smallest_even_value = arr[i]
                smallest_even_index = i
    
    if smallest_even_value is not None:
        return [smallest_even_value, smallest_even_index]
    else:
        return []

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([4,2,3]) == [2, 1], "Error"
    assert candidate([1,2,3]) == [2, 1], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3], "Error"
    assert candidate([5, 4, 8, 4 ,8]) == [4, 1], "Error"
    assert candidate([7, 6, 7, 1]) == [6, 1], "Error"
    assert candidate([7, 9, 7, 1]) == [], "Error"


check(pluck)