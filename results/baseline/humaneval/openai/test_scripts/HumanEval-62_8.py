def derivative(xs: list):
    return [xs[i+1]*(i+1) for i in range(len(xs)-1)]

# Test cases





METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []


check(derivative)