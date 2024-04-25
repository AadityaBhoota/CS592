from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The integer to be inserted between consecutive elements.

    Returns:
        List[int]: The new list with the delimeter inserted.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])

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