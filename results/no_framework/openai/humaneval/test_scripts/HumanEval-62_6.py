def derivative(xs: list):
    # Initialize an empty list to store the derivative coefficients
    derivative_coefficients = []
    
    # Iterate over the coefficients, excluding the constant term
    for i in range(1, len(xs)):
        # Multiply the coefficient by its corresponding power and append to the derivative list
        derivative_coefficients.append(xs[i] * i)
    
    return derivative_coefficients

# Test cases





METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []


check(derivative)