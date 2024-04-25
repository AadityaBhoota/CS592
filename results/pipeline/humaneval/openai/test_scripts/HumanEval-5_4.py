from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if num is not the last element
            result.append(delimiter)
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