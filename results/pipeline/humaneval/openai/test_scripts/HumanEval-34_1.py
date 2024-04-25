def unique(l: list):
    unique_set = set(l)
    unique_sorted = sorted(unique_set)
    return unique_sorted



METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)