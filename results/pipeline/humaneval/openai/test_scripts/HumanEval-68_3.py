def pluck(arr):
    min_even_value = None
    min_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0:  # Check if the value is even
            if min_even_value is None or value < min_even_value or (value == min_even_value and index < min_index): # Compare with current min_even_value
                min_even_value = value
                min_index = index

    if min_even_value is None:
        return []
    
    return [min_even_value, min_index]

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