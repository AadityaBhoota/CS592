    interspersed_list = []
    for num in numbers[:-1]:
        interspersed_list.extend([num, delimeter])
    if numbers:
        interspersed_list.append(numbers[-1])
    
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