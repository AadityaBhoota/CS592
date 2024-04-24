    interspersed_list = []
    for num in numbers:
        interspersed_list.append(num)
        interspersed_list.append(delimeter)
    interspersed_list.pop()  # remove the last delimiter
    return interspersed_list



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

check(intersperse)