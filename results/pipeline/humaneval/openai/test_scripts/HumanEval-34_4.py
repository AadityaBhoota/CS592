def unique(l: list):
    unique_elements = set(l)
    unique_elements_sorted = sorted(unique_elements)
    return unique_elements_sorted



METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)