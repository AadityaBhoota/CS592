def by_length(arr):
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    # Filter and sort the array
    filtered_arr = sorted([num for num in arr if 1 <= num <= 9])
    
    # Reverse sorted array and replace with names
    result = [names[num-1] for num in filtered_arr[::-1]]
    
    return result

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([1, -1 , 55]) == ['One'], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, -1, 3, 2]) == ["Three", "Two", "One"]
    assert candidate([9, 4, 8]) == ["Nine", "Eight", "Four"]


check(by_length)