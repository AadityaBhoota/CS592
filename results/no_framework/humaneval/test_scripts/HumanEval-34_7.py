def unique(l: list):
    unique_elements = list(set(l))  # Remove duplicates using a set
    unique_elements.sort()  # Sort the unique elements
    return unique_elements

# Test the function




METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)