from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`"""
    result = [num for i, num in enumerate(numbers) if i == 0 or i > 0]
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