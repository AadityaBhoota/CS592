def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_even_values = sorted([l[i] for i in even_indices])

    result = l.copy()
    for i, val in zip(even_indices, sorted_even_values):
        result[i] = val

    return result

# Test cases





METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])


check(sort_even)