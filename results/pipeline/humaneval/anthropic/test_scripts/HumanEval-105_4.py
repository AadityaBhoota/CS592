def by_length(arr):
    result = []
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    for num in reversed_arr:
        result.append(["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][num - 1])
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