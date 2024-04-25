from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list `numbers`."""
    result = []
    for num in numbers[:-1]:
        result.extend([num, delimiter])
    result.append(numbers[-1])  # Append the last number without delimiter
    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

check(intersperse)