def sort_third(l: list):
    result = []
    to_sort = []
    
    for i, val in enumerate(l):
        if i % 3 == 0:
            to_sort.append(val)
            result.append(None)  # Placeholder for values to be sorted later
        else:
            result.append(val)

    indices_to_sort = [i for i in range(len(l)) if i % 3 == 0]
    sorted_values = sorted(to_sort)

    for i, sorted_val in zip(indices_to_sort, sorted_values):
        result[i] = sorted_val

    final_result = [result[i] if i in indices_to_sort else val for i, val in enumerate(l)]

    return final_result



METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple(sort_third([1, 2, 3]))
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple(sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple(sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]))
    assert tuple(candidate([5, 6, 3, 4, 8, 9, 2])) == tuple([2, 6, 3, 4, 8, 9, 5])
    assert tuple(candidate([5, 8, 3, 4, 6, 9, 2])) == tuple([2, 8, 3, 4, 6, 9, 5])
    assert tuple(candidate([5, 6, 9, 4, 8, 3, 2])) == tuple([2, 6, 9, 4, 8, 3, 5])
    assert tuple(candidate([5, 6, 3, 4, 8, 9, 2, 1])) == tuple([2, 6, 3, 4, 8, 9, 5, 1])


check(sort_third)