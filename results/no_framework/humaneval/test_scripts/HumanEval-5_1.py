    interspersed_numbers = []
    for num in numbers:
        interspersed_numbers.append(num)
        if num != numbers[-1]:
            interspersed_numbers.append(delimeter)
    
    return interspersed_numbers



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

check(intersperse)