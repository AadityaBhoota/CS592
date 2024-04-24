def prod_signs(arr):
    if not arr:
        return None
    
    product = 1
    total = 0
    for num in arr:
        if num > 0:
            total += num
        elif num < 0:
            total -= num
            product *= -1

    return total * product

# Test the function with the provided examples
print(prod_signs([1, 2, 2, -4]))  # Output: -9
print(prod_signs([0, 1]))          # Output: 0
print(prod_signs([]))              # Output: None

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 1]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([]) == None
    assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
    assert candidate([-1, 1, -1, 1]) == 4
    assert candidate([-1, 1, 1, 1]) == -4
    assert candidate([-1, 1, 1, 0]) == 0

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(prod_signs)