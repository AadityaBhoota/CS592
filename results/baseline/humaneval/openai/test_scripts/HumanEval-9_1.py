from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if len(numbers) == 0:
        return []

    result = [numbers[0]]
    maximum = numbers[0]

    for num in numbers[1:]:
        maximum = max(maximum, num)
        result.append(maximum)

    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]

check(rolling_max)