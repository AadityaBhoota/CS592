def sort_even(l: list):
    sorted_even_vals = []  # Step 0

    for idx, val in enumerate(l):  # Step 1
        if idx % 2 == 1:  # Step 2
            sorted_even_vals.append(val)  # Step 2
        else:  # Step 3
            sorted_even_vals.append(sorted(l[:idx+1]))  # Step 3

    return sorted_even_vals  # Step 4



METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])


check(sort_even)