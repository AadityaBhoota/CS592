def unique(l):
    return sorted(set(l))

# Test the function with the given example
result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])




METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)