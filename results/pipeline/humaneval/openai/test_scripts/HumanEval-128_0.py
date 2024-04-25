def prod_signs(arr):
    if not arr:  # Step 0: Check if the input array is empty
        return None
    
    result = 0  # Step 1: Initialize a variable `result` to 0
    sum_magnitude = 0  # Step 4: Initialize a variable `sum_magnitude` to 0
    
    for num in arr:
        # Step 2: Calculate the product of signs and sum of magnitudes concurrently
        if num > 0:
            result += num
            sum_magnitude += abs(num)
        elif num < 0:
            result -= num
            sum_magnitude += abs(num)
    
    return result  # Step 3: Return the `result`

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