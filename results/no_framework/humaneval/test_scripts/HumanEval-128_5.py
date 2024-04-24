def prod_signs(arr):
    if not arr:
        return None
    
    positives = [x for x in arr if x > 0]
    negatives = [x for x in arr if x < 0]

    product_signs = 1
    if len(positives) % 2 == 1:
        product_signs *= 1
    if len(negatives) % 2 == 1:
        product_signs *= -1

    total_magnitude = sum(abs(x) for x in arr)

    return product_signs * total_magnitude

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