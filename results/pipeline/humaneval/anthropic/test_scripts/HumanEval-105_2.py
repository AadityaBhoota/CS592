def by_length(arr):
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    valid_digits = [d for d in arr if 1 <= d <= 9]
    valid_digits.sort()
    valid_digits.reverse()
    transformed_digits = [digit_names[d-1] for d in valid_digits]
    return transformed_digits

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