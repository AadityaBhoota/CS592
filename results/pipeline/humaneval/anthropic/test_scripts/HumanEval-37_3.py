def sort_even(l: list):
    result = []
    even_values = []
    for i, value in enumerate(l):
        if i % 2 == 0:
            even_values.append(value)
        else:
            result.append(value)
    even_values.sort()
    even_index = 0
    for i in range(len(result)):
        if i % 2 == 0:
            result[i] = even_values[even_index]
            even_index += 1
    return result



METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])


check(sort_even)