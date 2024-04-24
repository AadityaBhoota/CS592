def derivative(xs: list):
    derivative_result = [xs[i] * i for i in range(1, len(xs))]
    return derivative_result

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []


check(derivative)